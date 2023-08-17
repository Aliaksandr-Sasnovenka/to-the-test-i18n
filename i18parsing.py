"""This script provides an approach to know if there are any files that contain the error lack of i18n tag."""
import glob
import re

# tag list for checking
TAG_LIST = ["p", "button", "h2", "h"]
_FILE_EXT = "html"
PROP = "i18n"


# getting a list of interested files
def get_of_curious_files(file_ext: str):
    files = glob.glob(f'./**/*.{file_ext}', recursive=True)
    return files


# regular expression core
def missing_property(input_file, prop: str):
    line_pointer = {}  # a line counter
    for file in input_file:
        with open(file, "r") as f:
            line = f.readline()
            line_counter = 0
            while line:  # take a generator mode
                line_counter += 1
                raw_tag = re.search("<.*?>", line)
                for tag in TAG_LIST:  # we are forced to loop over tag list every time cose strings are dirty
                    if str(raw_tag).__contains__(f"<{tag}"):
                        # Seeking the right match of implemented property
                        is_prop_here = str(raw_tag).__contains__(f"{prop}")
                        if not is_prop_here:  # we are here if strings are tidy
                            line_pointer.update({f"{f.name}": f"{line_counter}"})  # i18n is missed
                            break
                line = f.readline()
    return line_pointer


# How is it working?
print(missing_property(get_of_curious_files(_FILE_EXT), PROP))
