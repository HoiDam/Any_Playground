import base64
authx   = 'Basic ' + base64.b64encode(('riot:' + "-dyzz5Bs0kvR32n3zRYtBw").encode(encoding = 'utf-8')).decode('utf-8')
print(authx)