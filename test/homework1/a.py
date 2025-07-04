freeze = 'freeze'# — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так не больше желаемой, то он выключается.
heat = 'heat'# — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не меньше желаемой, то он выключается.
auto = 'auto'# — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате до желаемой.
fan = 'fan' # - вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в комнате.

t = input().split(' ')
troom = int(t[0])
tcond = int(t[1])
method = input()
result = 0

if tcond < -50:
    tcond = -50
if tcond > 50:
    tcond = 50
    
if troom < -50:
    troom = -50
if troom > 50:
    troom = 50

if method == freeze:
    result = min(troom, tcond)
elif method == heat:
    result = max(troom, tcond)
elif method == auto:
    result = tcond
elif method == fan:
    result = troom

print(result)