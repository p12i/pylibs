class Action(object):
    description = ''
    subparsers = None

    def __init__(self, parser):
        self.parser = parser
        self.register_subparser()
        self.register_arguments()

    def get_subparsers(self):
        if Action.subparsers is None:
            Action.subparsers = self.parser.add_subparsers()
        return Action.subparsers

    def register_subparser(self):
        sb = self.get_subparsers()
        self.local_parser = sb.add_parser(self.name, help=self.description)
        self.local_parser.set_defaults(func=self)

    def __call__(self, args):
        self.args = args
        self.root_dir = args.root_dir
        self.archive_dir = args.archive_dir
        return self.run()

    # Funkcja do przeciazenia
    def run(self):
        pass

    # Funkcja do przeciazenia
    def register_arguments(self):
        pass
