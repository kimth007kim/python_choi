breads= ['호밀빵','위트','화이트']
meats= ['미트볼','소시지','닭가슴살']
vegitables=['양상추','토마토','오이']
sauces=['마요네즈','허니머스타드','칠리']

for b in breads:
    for m in meats:
        for v in vegitables:
            for s in sauces:
                print(b+"+"+m+"+"+v+"+"+s)