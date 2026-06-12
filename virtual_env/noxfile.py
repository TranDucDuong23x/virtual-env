import nox #type:ignore
@nox.session(python="3.14")
def tests(session):
    session.install("pytest")
    session.install("requests")
    session.install("uv")
    # session.run("pytest", "-v", "tests/test_demo2.py")
    # session.run("pytest","tests/test_demo2.py","-m","slow")
    # session.run("pytest","tests/test_demo2.py","-m","xfail")
    # session.run("pytest","tests/test_demo2.py","-m","skip")
    # session.run("pytest","-v","tests/test_demoOOP.py")
    # session.run('pytest','-v','tests/test_mock.py')
    session.run('uv','python','list')