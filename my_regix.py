import re

# ###############################################################
with open('show_ver.txt','r') as file:
# #     my_pattern= r'Cisco'
# #     print(re.search(my_pattern,file.read()).group(0))

# ###############################################################
    my_pattern=r'[Cc]isco.+, Version (\d\S+)'
    file_data=file.read()
    version_output= re.search(my_pattern,file_data).group(1)
    print(f"{'version:'.ljust(18)}: {version_output}".rstrip(','))

##############################################################


