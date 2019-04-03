name = eval( '[' + open( 'D:\Python-learning\some-example\problrm22\p022_names.txt' ).readlines()[ 0 ] + ']' )
name.sort()

ans = 0
for i in range(len(name)):
    mul = 0
    for j in range(len(name[i])):
        mul += ord(name[i][j]) - ord('A') + 1
    mul *= (i + 1)
    ans += mul

print(ans)
