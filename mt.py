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
