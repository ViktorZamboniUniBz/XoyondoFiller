import re

def create_xoyondo_pattern():
    return re.compile(r'https?://(?:www\.)?xoyondo\.com/op/\S+')
