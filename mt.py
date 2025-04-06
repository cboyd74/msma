import curses

from src.exception.input_exception import InvalidInputException, EmptyInputException, InvalidCommandException, \
    InputException
from src.service.app_logger import AppLogger
from src.model.command import Command
from src.model.session import Session
from src.service.music_interface import get_fretboard, get_new_key, get_key_data, toggle_mode, get_key_name, \
    relative_is_available, get_random_key
from src.ui.curses_ui import refresh_screen, print_help, toggle_relative, print_error

logger = AppLogger.get_logger()


def setup_light_mode_colors():
    curses.start_color()
    curses.use_default_colors()

    # Define custom colors (index, R, G, B in 0-1000 range)
    curses.init_color(10, 950, 930, 850)  # Soft warm beige
    curses.init_color(11, 133, 133, 133)  # Dark Charcoal text
    curses.init_color(12, 333, 333, 333)  # Muted Gray
    curses.init_color(13, 184, 502, 929)  # Accent Blue
    curses.init_color(14, 866, 866, 866)  # Light Gray
    curses.init_color(15, 827, 184, 184)  # Error Red
    curses.init_color(16, 219, 557, 235)  # Success Green
    curses.init_color(17, 1000, 980, 803)  # Pale Yellow

    # Define color pairs (pair number, foreground, background)
    curses.init_pair(1, 11, 10)  # Primary Text on Background
    curses.init_pair(2, 12, 10)  # Secondary Text
    curses.init_pair(3, 13, 10)  # Accent
    curses.init_pair(4, 15, 10)  # Error
    curses.init_pair(5, 16, 10)  # Success
    curses.init_pair(6, 11, 14)  # Border / lines
    curses.init_pair(7, 11, 17)  # Prompt Input Box


def setup_dark_mode_colors():
    # Initialize dark colors
    curses.init_color(10, 100, 100, 100)  # Dark grey background
    curses.init_color(11, 900, 900, 900)  # Soft white text
    curses.init_color(12, 400, 600, 900)  # Slate blue accent (e.g., headings, links)
    curses.init_color(13, 400, 700, 500)  # Muted green (success)
    curses.init_color(14, 900, 400, 400)  # Muted red (error)
    curses.init_color(15, 900, 800, 500)  # Muted yellow (warning)

    # Initialize color pairs
    curses.init_pair(1, 11, 10)  # White text on dark grey background
    curses.init_pair(2, 12, 10)  # Slate blue on dark grey
    curses.init_pair(3, 13, 10)  # Green on dark grey
    curses.init_pair(4, 14, 10)  # Red on dark grey
    curses.init_pair(5, 15, 10)  # Yellow on dark grey


# Main function ###############################################
def main(stdscr):
    logger.debug('Starting app...')
    # Define color pairs (foreground, background)
    setup_dark_mode_colors()
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
