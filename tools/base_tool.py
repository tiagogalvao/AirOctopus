import subprocess


class BaseTool:
    assembly_name = ''

    def check_existence(self):
        result = False
        try:
            if len(self.assembly_name) > 0:
                subprocess.check_output(['which', self.assembly_name])
                result = True
        except subprocess.CalledProcessError:
            result = False

        return result
