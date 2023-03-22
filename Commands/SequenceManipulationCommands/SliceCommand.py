from Commands.SequenceManipulationCommands.SequenceManipulationCommands import SequenceManipulationCommands


class SliceCommand(SequenceManipulationCommands):
    def __init__(self):
        self.suffix = '_s1'

    def execute(self, *args):
        return super().execute(*args)

    def manipulate(self, command, sequence):
        slices_limits = len(command) - 2 if command[-2] == ':' else len(command)
        new_sequence = ''
        try:
            for i in range(1, slices_limits, 2):
                new_sequence += sequence[int(command[i]): int(command[i + 1])]
            return new_sequence
        except IndexError:
            return None
