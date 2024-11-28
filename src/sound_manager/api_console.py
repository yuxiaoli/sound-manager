import cmd2

from sound_manager.buffered_cmd2 import BufferedCmd#, Result
from sound_manager.sound import Sound

class Console(BufferedCmd):
    # CMD_CATEGORY = "Admin Commands"
    CMD_CATEGORY = "Sound Commands"
    def __init__(
        self, 
        *args, 
        **kwargs
    ) -> None:
        super().__init__(
            *args, 
            **kwargs
        )
        self.prompt = "Sound Manager> "
        self.intro = cmd2.style('Welcome to Windows Sound Manager (Python 3)', fg=cmd2.Fg.GREEN, bold=True)
        # self.debug = True

        # https://cmd2.readthedocs.io/en/latest/features/settings.html
        self.settable_value = 12
        self.add_settable(cmd2.Settable("settable_value", str, "Settable value description", self))

    @cmd2.with_category(CMD_CATEGORY)
    def do_mute(self, args):
        """Mute or unmute the volume."""
        Sound.mute()

    @cmd2.with_category(CMD_CATEGORY)
    def do_volume_up(self, args):
        """Increase the volume."""
        Sound.volume_up()

    @cmd2.with_category(CMD_CATEGORY)
    def do_volume_down(self, args):
        """Decrease the volume."""
        Sound.volume_down()

    @cmd2.with_category(CMD_CATEGORY)
    def do_volume_min(self, args):
        """Set the volume to 0."""
        Sound.volume_min()

    @cmd2.with_category(CMD_CATEGORY)
    def do_volume_max(self, args):
        """Set the volume to 100."""
        Sound.volume_max()

    volume_set_parser = cmd2.Cmd2ArgumentParser()
    volume_set_parser.add_argument('value', type=int, help='Volume level (0-100)')
    @cmd2.with_argparser(volume_set_parser)
    @cmd2.with_category(CMD_CATEGORY)
    def do_volume_set(self, args):
        """Set the volume to a specific level (0-100)."""
        Sound.volume_set(args.value)

    @cmd2.with_category(CMD_CATEGORY)
    def do_status(self, args):
        """Print the current sound settings."""
        print("Current volume | %s" % str(Sound.current_volume()))
        print("Sound muted    | %s" % str(Sound.is_muted()))
        print("----------------------")

    @cmd2.with_category(CMD_CATEGORY)
    def do_quit(self, args):
        """Quit the Sound Manager."""
        return True

# CONFIG = r"D:\wechat\configs\config.yaml"
def main():
    import sys
    c = Console()#config=CONFIG)
    # c.init(mode="admin")
    sys.exit(c.cmdloop())

if __name__ == "__main__":
    main()