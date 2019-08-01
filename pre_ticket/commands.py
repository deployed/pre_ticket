import subprocess


def call_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    returncode = process.wait()

    if returncode != 0:
        raise RuntimeError(
            "The command: {} failed with error code: {}".format(cmd, returncode)
        )

    out = out.strip()
    if not isinstance(out, str):
        out = out.decode("utf-8")

    return out
