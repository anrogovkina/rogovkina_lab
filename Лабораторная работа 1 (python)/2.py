# TODO Найдите количество книг, которое можно разместить на дискете
volume=1.44
pages=100
lines=50
symbols=25
symbols_volume=4
volume_bytes=volume*1024*1024
book_symbols=pages*lines*symbols
book_volume=book_symbols*symbols_volume
book_amount=round(volume_bytes/book_volume)
print("Количество книг, помещающихся на дискету:", book_amount)
