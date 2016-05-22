from subprocess import call
from scloud.settings import BASE_DIR
loc = BASE_DIR

# print BASE_DIR
# 	call (['ls' ,'"%s"' % loc],shell=True)
# print ("export $(cat BASE_DIR/.env)".split())
call (['export', '$(cat', '"%s"/.env)'%loc],shell=True)

print ("Env Variables Exported")