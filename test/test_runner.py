import unittest
import coverage

cov = coverage.Coverage(omit=['*test*.py', '__init__.py'])
cov.start()
# Discover and load all test files in the test directory and subdirectories
loader = unittest.TestLoader()
suite = loader.discover(start_dir='./', pattern='test_*.py')

# Run the test suite
runner = unittest.TextTestRunner()
runner.run(suite)

cov.stop()
cov.save()

# Generate coverage report
cov.report()
# cov.html_report()
