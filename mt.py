import curses
import json
from time import sleep

from src.config.constants import MAJOR_SCALE_ONLY, HAS_BLUES
from src.exception.input_exception import InvalidInputException, EmptyInputException, InvalidCommandException, \
    InputException
from src.model.mode import Mode
from src.service.app_logger import AppLogger
from src.model.command import Command
from src.model.session import Session, Input, Component
from src.service.music_interface import get_fretboard, get_new_key, get_key_data, toggle_mode, \
    is_valid_key, get_key_name, relative_is_available, get_random_key
from src.util.helpers import left_string_x, right_string_x, center_string_x, get_traditional_roots, center_string_y

TITLE = 'MSMA (My Shitty Music App)'
DIVIDER_WIDTH = 50
HEADER_SIZE = 3
FOOTER_SIZE = 1
STANDARD_SPACING = 3

logger = AppLogger.get_logger()


# TODO add better logging


def get_commands(session: Session) -> [str]:
    commands = ['[q] to quit', '[h] for help']
    if relative_is_available(session.get_key()):
        commands.append('[r] to toggle relative')
    commands.append('[p] to toggle pentatonic')
    commands.append('[b] to toggle blues')
    commands.append('[m] to toggle mode')
    commands.reverse()
    return commands


# Input functions ###############################################
def get_user_input(session: Session) -> Input:
    input_obj = Input()
    writer = session.get_writer()
    input_y, input_x = session.get_input_y_x()
    input_str = writer.getstr(input_y, input_x).decode('utf-8').strip()
    input_obj.set_input(input_str)
    return input_obj


# Helpers ####################################################
def print_line(line: str, y: int, x: int, session: Session):
    writer = session.get_writer()
    writer.addstr(y, x, line)
    writer.refresh()


def print_line_centered_x(line: str, y: int, start_x: int, end_x: int, session: Session):
    x = center_string_x(line, start_x, end_x) + start_x + 1
    print_line(line, y, x, session)


def print_line_left_x(line: str, y: int, start_x: int, session: Session):
    x = left_string_x(start_x)
    print_line(line, y, x, session)


def print_borders(component: Component, session: Session):
    logger.debug('Printing borders...')
    min_y = component.get_start_y()
    max_y = component.get_end_y()
    min_x = component.get_start_x()
    max_x = component.get_end_x()
    logger.info(f'Min_Y: {min_y}, Max_Y: {max_y}, Min_X: {min_x}, Max_X: {max_x}')
    for y in range(min_y, max_y + 1):
        print_line('|', y, min_x, session)
        print_line('|', y, max_x, session)
    for x in range(min_x, max_x + 1):
        print_line('-', min_y, x, session)
        print_line('-', max_y, x, session)


def print_divider(y: int, start_x: int, end_x: int, session: Session):
    print_line_centered_x('-' * DIVIDER_WIDTH, y, start_x, end_x, session)


def print_centered_list(list_to_print: [], start_y, start_x, end_x, session: Session):
    lines = []
    lowest_center_x = 1_000_000
    for i, item in enumerate(list_to_print):
        line = f'[{i}] {item}'
        lines.append(line)
        center_x = center_string_x(line, start_x, end_x)
        lowest_center_x = min(lowest_center_x, center_x)
    current_y = start_y
    for line in lines:
        print_line(line, current_y, lowest_center_x, session)
        current_y += 1


def fill_rectangle(component: Component, session: Session):
    start_y = component.get_start_y() + 1
    end_y = component.get_end_y() - 1
    start_x = component.get_start_x() + 1
    end_x = component.get_end_x() - 1
    writer = session.get_writer()
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            writer.addstr(y, x, ' ')


def get_roots_str(session: Session) -> str:
    roots_str = ' '
    current_root = get_key_data(session.get_key()).get('root')
    for root in get_traditional_roots():
        if root == current_root:
            roots_str += f'   [{root}]   '
        else:
            roots_str += f'    {root}    '
    return roots_str.strip()


def get_mode_str(session: Session) -> str:
    key_data = get_key_data(session.get_key())
    if not key_data:
        return "Major | Minor "
    mode = key_data.get('mode')
    has_minor = key_data.get('has_minor')
    return (
        f'{"[Major]" if mode == Mode.MAJOR else "Major"} '
        f'{"| [Minor]" if has_minor and mode == Mode.MINOR else "| Minor" if has_minor else ""}'
    )


def get_pent_blues_string(session: Session) -> str:
    key_data = get_key_data(session.get_key())
    if not key_data:
        return "Pentatonic | Blues "
    has_blues = key_data.get('has_blues')
    logger.debug(f'Key Data: {key_data}')
    return (
        f'{"[Pentatonic]" if session.is_pentatonic() else "Pentatonic"}'
        f' {"| [Blues]" if session.is_blues() and has_blues else "| Blues" if has_blues else ""}'
    )


# Print page functions ##########################################
def print_header(session: Session):
    logger.debug('Printing header...')
    start_x, end_x = session.get_x_min_max_safe()
    start_y, end_y = session.get_y_min_max_safe()
    end_y = start_y + HEADER_SIZE
    w = end_x - start_x
    logger.info(f'Start_Y: {start_y}, End_Y: {end_y}, Start_X: {start_x}, End_X: {end_x}')
    key = session.get_key()
    left_x = left_string_x(start_x)
    print_line(TITLE, start_y + 1, left_x, session)
    display_key = f'Key: {get_key_name(key)}'
    right_x = right_string_x(display_key, start_x, end_x)
    print_line(display_key, start_y + 1, right_x, session)
    logger.debug(f"start_x: {start_x}, end_x: {end_x}")
    print_line('-' * w, start_y + 3, start_x, session)


def print_footer(session: Session):
    logger.debug('Printing footer...')
    _, end_y = session.get_y_min_max_safe()
    start_y = end_y - FOOTER_SIZE
    start_x, end_x = session.get_x_min_max_safe()
    logger.debug(f'Start_X: {start_x}, End_X: {end_x}')
    input_y, input_x = session.get_input_y_x()
    w = end_x - start_x
    print_line('-' * w, start_y, start_x, session)
    print_line(':', input_y, input_x - 1, session)
    cmds = get_commands(session)
    foot_str = '  '.join(cmds)
    start_x_right = right_string_x(foot_str, start_x, end_x)
    print_line(foot_str, input_y, start_x_right, session)


def print_error(session: Session, message: str):
    logger.debug('Printing error...')
    safe_x_start, safe_x_end = session.get_x_min_max_safe()
    screen_height, _ = session.get_height_width()

    w = 100
    h = 16
    start_x = center_string_x('-' * w, safe_x_start, safe_x_end)
    end_x = start_x + w
    start_y = int(round(screen_height * 0.28, 0))
    end_y = start_y + h

    component = Component(start_y=start_y, end_y=end_y, start_x=start_x, end_x=end_x)

    print_borders(component, session)
    fill_rectangle(component, session)

    print_line_centered_x('Error', component.get_start_y() + 1, component.get_start_x(), component.get_end_x(), session)
    print_line_centered_x('-' * (w - 1), component.get_start_y() + 2, component.get_start_x(), component.get_end_x(),
                          session)
    print_line_centered_x(f'{message}', component.get_start_y() + 5, component.get_start_x(), component.get_end_x(), session)
    print_line_left_x('Press any key to continue...', component.get_end_y() - 1, component.get_start_x(), session)
    session.get_writer().getch()


def print_help(session: Session, message: str):
    logger.debug('Printing help...')
    safe_x_start, safe_x_end = session.get_x_min_max_safe()
    screen_height, _ = session.get_height_width()

    w = 100
    h = 30
    start_x = center_string_x('-' * w, safe_x_start, safe_x_end)
    end_x = start_x + w
    start_y = int(round(screen_height * 0.25, 0))
    end_y = start_y + h

    component = Component(start_y=start_y, end_y=end_y, start_x=start_x, end_x=end_x)
    logger.debug(f'Help page component: {json.dumps(component.__dict__)}')

    # Prepare window
    print_borders(component, session)
    fill_rectangle(component, session)
    print_line_centered_x('Help', component.get_start_y() + 1, component.get_start_x(), component.get_end_x(), session)
    print_line_centered_x('-' * (w - 1), component.get_start_y() + 2, component.get_start_x(), component.get_end_x(),
                          session)

    content_start_y = component.get_start_y() + 3
    print_line_left_x('[System Commands]', content_start_y, component.get_start_x(), session)
    print_line_left_x(' [q] to quit the application', content_start_y + 2, component.get_start_x(), session)
    print_line_left_x(' [m] to toggle between major and minor scales', content_start_y + 3, component.get_start_x(),
                      session)
    print_line_left_x(' [p] to toggle pentatonic scale on/off - [Pentatonic]/Pentatonic', content_start_y + 4,
                      component.get_start_x(), session)
    print_line_left_x(' [b] to toggle blues scales on/off - [Blues]/Blues (if available)', content_start_y + 5,
                      component.get_start_x(),
                      session)
    print_line_left_x(' [r] to jump to relative key (if available)', content_start_y + 6, component.get_start_x(),
                      session)

    print_line_left_x('[Available Root Notes]', content_start_y + 9, component.get_start_x(), session)
    print_line_left_x(' This application supports the following root notes:', content_start_y + 11,
                      component.get_start_x(), session)
    print_line_left_x(f' {"    ".join(get_traditional_roots())}', content_start_y + 12, component.get_start_x(),
                      session)
    print_line_left_x(
        ' Jump between different root notes by typing them exactly as seen on the screen',
        content_start_y + 13, component.get_start_x(), session)

    print_line_left_x('[Roots without minor scales]', content_start_y + 16, component.get_start_x(), session)
    print_line_left_x(f' The following root notes do not have minor scales: {"    ".join(MAJOR_SCALE_ONLY)}',
                      content_start_y + 18,
                      component.get_start_x(), session)

    print_line_left_x('[Blues Scales] - only available for the most common blues keys', content_start_y + 21,
                      component.get_start_x(), session)
    print_line_left_x(f' Major keys: {"    ".join(HAS_BLUES.get(Mode.MAJOR))}', content_start_y + 23,
                      component.get_start_x(), session)
    print_line_left_x(f' Minor keys: {"    ".join(HAS_BLUES.get(Mode.MINOR))}', content_start_y + 24,
                      component.get_start_x(), session)

    print_line_left_x('Press any key to continue...', component.get_end_y() - 1, component.get_start_x(), session)
    session.get_writer().getch()


def print_options(component: Component, session: Session):
    logger.debug('Printing options...')
    start_y = component.get_start_y()
    start_x = component.get_start_x()
    logger.info(f'Start_Y: {start_y}')

    roots_str = get_roots_str(session)
    mode_str = get_mode_str(session)
    pent_blues_string = get_pent_blues_string(session)

    print_line_left_x(roots_str, start_y, start_x, session)
    print_line_left_x(mode_str, start_y + 2, start_x, session)
    print_line_left_x(pent_blues_string, start_y + 4, start_x, session)


def print_home_graphic(component: Component, session: Session):
    logger.debug('Printing homepage...')
    start_y = component.get_start_y()
    start_x = component.get_start_x()
    end_x = component.get_end_x()

    print_line_centered_x(f'Welcome to MSMA', start_y + 1, start_x, end_x, session)
    print_line_centered_x(f'Press any key to get started...', start_y + 3, start_x, end_x, session)
    key = get_random_key()
    fretboard = get_fretboard(key, False, False)
    base = start_y + 7
    for string in fretboard:
        print_line_centered_x(string, base, start_x, end_x, session)
        base += 1


def print_key(component: Component, session: Session):
    start_y = component.get_start_y()
    start_x = component.get_start_x()
    end_x = component.get_end_x()

    key = session.get_key()
    key_data = get_key_data(key, session.is_pentatonic(), session.is_blues())
    scale = key_data.get('scale')
    steps = key_data.get('steps')
    chords = key_data.get('chords')
    chord_pattern = key_data.get('chord_pattern')
    relative_key = key_data.get('relative')

    chords_rom_str = ' - '.join(chord_pattern)
    notes = ' - '.join(scale)
    steps_str = ' - '.join(steps)
    chords_str = ' - '.join(chords)

    notes_line_y = start_y + 8
    steps_line_y = start_y + 6
    chord_pattern_y = start_y + 11
    chords_line_y = start_y + 13

    print_line_centered_x(f'Key: {get_key_name(key)}', start_y, start_x, end_x, session)
    print_line_centered_x(f'Relative: {get_key_name(relative_key) if is_valid_key(relative_key) else "Not Available"}',
                          start_y + 2, start_x, end_x, session)

    print_line_centered_x(steps_str, steps_line_y, start_x, end_x, session)
    print_line_centered_x(chords_rom_str, chord_pattern_y, start_x, end_x, session)
    print_line_centered_x(notes, notes_line_y, start_x, end_x, session)
    print_line_centered_x(chords_str, chords_line_y, start_x, end_x, session)

    label_start = center_string_x(notes, start_x, end_x) - 20

    print_line('Notes: ', notes_line_y, label_start, session)
    print_line('Steps: ', steps_line_y, label_start, session)
    print_line('Chords: ', chords_line_y, label_start, session)

    fretboard = get_fretboard(key, session.is_pentatonic(), session.is_blues())
    base = start_y + 18
    for string in fretboard:
        print_line_centered_x(string, base, start_x, end_x, session)
        base += 1


# Main app functions ###########################################
def print_homepage(component: Component, session: Session):
    logger.debug('Printing homepage...')
    session.get_writer().nodelay(1)
    while True:
        print_home_graphic(component, session)
        sleep(1)
        ch = session.get_writer().getch()
        if ch != -1:  # If input is available
            input_obj = Input()
            input_obj.set_input('C')
            session.set_previous_input(input_obj)
            session.get_writer().nodelay(0)
            break


def main_page(session: Session, component: Component):
    logger.debug('Printing main page...')
    print_key(component, session)
    # Collect input
    inp_obj = get_user_input(session)
    session.set_previous_input(inp_obj)


def content(session: Session, component: Component):
    logger.debug('Printing content...')
    start_y = component.get_start_y() + HEADER_SIZE + STANDARD_SPACING
    end_y = component.get_end_y() - FOOTER_SIZE
    component.set_start_y(start_y)
    component.set_end_y(end_y)
    print_options(component, session)
    main_start_y = start_y + 5 + STANDARD_SPACING
    component.set_start_y(main_start_y)
    # if key is not selected, prompt user to select a key
    if not is_valid_key(session.get_key()):
        print_homepage(component, session)
    else:
        main_page(session, component)


def refresh_screen(session: Session):
    logger.debug('Refreshing screen...')
    writer = session.get_writer()
    writer.clear()
    # get screen dimensions
    h, w = writer.getmaxyx()
    logger.debug(f'Height: {h}, Width: {w}')
    session.set_dimensions(h, w)
    min_y, max_y, min_x, max_x = session.get_y_x_min_max()
    component = Component(start_y=min_y, end_y=max_y, start_x=min_x, end_x=max_x)
    # print boarders, header, footer
    print_borders(component, session)
    print_header(session)
    print_footer(session)
    min_y, max_y, min_x, max_x = session.get_y_x_min_max_safe()
    component = Component(start_y=min_y, end_y=max_y, start_x=min_x, end_x=max_x)
    content(session, component)
    writer.refresh()


# App helpers ################################################
def toggle_relative(session: Session) -> Session:
    logger.debug('Toggling relative...')
    key = session.get_key()
    if is_valid_key(key):
        key_data = get_key_data(key)
        new_key = key_data.get('relative')
        session.set_key(new_key)
    return session


# Main function ###############################################
def main(stdscr):
    logger.debug('Starting app...')
    # Define color pairs (foreground, background)
    curses.init_color(10, 0, 51, 0)
    curses.init_pair(1, curses.COLOR_WHITE, 10)
    # Set the background color
    stdscr.bkgd(' ', curses.color_pair(1))
    curses.curs_set(0)  # Hide the cursor
    curses.echo()
    session = Session(stdscr)
    try:
        while True:
            refresh_screen(session)
            try:
                # process cmd
                input_obj = session.get_previous_input()
                # Update key logic #####################################
                if input_obj.is_empty():
                    logger.debug('Empty input...')
                    raise EmptyInputException('Empty input')
                elif input_obj.is_update_key():
                    logger.debug('Updating key...')
                    key = get_new_key(input_obj.get_value())
                    session.set_key(key)
                # System commands ####################################
                elif input_obj.is_cmd():
                    cmd = input_obj.get_value()
                    if cmd == Command.QUIT:
                        logger.debug('Quitting...')
                        break
                    elif cmd == Command.HELP:
                        logger.debug('Help...')
                        print_help(session, 'Help not available yet')
                    elif cmd == Command.TOGGLE_MODE:
                        logger.debug('Toggling mode...')
                        key_data = get_key_data(session.get_key())
                        if key_data.get('has_minor'):
                            toggle_mode(session.get_key())
                        else:
                            raise InvalidCommandException(f'Minor not available for {key_data.get("root")}')
                    elif cmd == Command.TOGGLE_PENTATONIC:
                        logger.debug('Toggling pentatonic...')
                        session.toggle_pentatonic()
                    elif cmd == Command.TOGGLE_RELATIVE:
                        logger.debug('Toggling relative...')
                        if relative_is_available(session.get_key()):
                            session = toggle_relative(session)
                        else:
                            raise InvalidCommandException(
                                f'Relative key not available for {get_key_name(session.get_key())}')
                    elif cmd == Command.TOGGLE_BLUES:
                        logger.debug('Toggling blues...')
                        if get_key_data(session.get_key()).get('has_blues'):
                            session.toggle_blues()
                        else:
                            raise InvalidCommandException(f'Blues not available for {get_key_name(session.get_key())}')
                # Anything else is INVALID ###############################
                else:
                    raise InvalidInputException(f'Invalid input: {input_obj.get_value()}')
            except InputException as e:
                logger.info(f'InputException: {e.message}')
                print_error(session, e.message)
    except Exception as e:
        logger.exception(f'Fatal error occurred: {e}')


# Run the program #############################################
curses.wrapper(main)
