books = [
    {
        'title': 'Harry Potter',
        'genre': 'Fantasy',
        'author': 'J. K. Rowlings',
        'available': True
    },
    {
        'title': 'Twilight',
        'genre': 'Romance',
        'author': 'Stephenie Meyer',
        'available': True
    },
    {
        'title': 'Hunger Games',
        'genre': 'Fiction',
        'author': 'Suzanne Collins',
        'available': False
    },
    {
        'title': 'Fifty Shades of Grey',
        'genre': 'Romance',
        'author': 'E. L. James',
        'available': True
    }
]

adminPassword = 'JCDSOL08'

def read(booksList, genre=False, checkAvailable=False):
    if len(booksList) == 0:
        print('Tidak ada data')

    elif type(genre) == int:
        counter = 0
        for i in booksList:
            if i['genre'] == getGenres(booksList)[genre]:
                counter += 1
                print(f'{"="*12} {counter} {"="*12}')
                for key in i:
                    print(f'{key.capitalize()} : {i[key]}')
                print(f'{"="*27}\n')
    
    elif checkAvailable:
        counter = 0
        for i in booksList:
            if i['available'] == True:
                counter += 1
                print(f'{"="*12} {counter} {"="*12}')
                for key in i:
                    print(f'{key.capitalize()} : {i[key]}')
                print(f'{"="*27}\n')

    else:
        counter = 0
        for i in booksList:
            counter += 1
            print(f'{"="*10} {counter} {"="*10}')
            for key in i:
                print(f'{key.capitalize()} : {i[key]}')
            print(f'{"="*23}\n')


def getGenres(booksList):
    genres = []
    for i in booksList:
        if i['genre'] not in genres:
            genres.append(i['genre'])
    return genres

def showGenres(genreList):
    for i in range(len(genreList)):
        print(i+1, f'. {genreList[i]}')

def checkDuplicate(booksList, bookTitle):
    for i in booksList:
        if i['title'].lower() == bookTitle.lower():
            return True    
    return False

def readAvailable(bookList):
    availableBooks = []
    for i in bookList:
        if i['available'] == True:
            availableBooks.append(i)
    return availableBooks

def create(title, genre, author):
    books.append({
        'title': title,
        'genre': genre,
        'author': author,
        'available': True
    })

def pickBook(booksList, order):
    return booksList[order-1]

def update(intBook, title=False, genre=False, author=False):
    editBook = pickBook(books, intBook)
    if title:
        editBook['title'] = title
    elif genre:
        editBook['genre'] = genre
    elif author:
        editBook['author'] = author
    return print('Data buku berhasil di-update')
        
def confirm(intInput):
    if intInput == '1':
        return True
    elif intInput == '2':
        return False
    else:
        print('Mohon hanya masukkan input 1 atau 2')

def borrow(booksList, intBook):
    pickBook(booksList, intBook)['available'] = False
    return print(f'Buku berhasil dipinjam')

def delete(booksList, intBook):
    booksList.pop(intBook-1)
    return print('Buku berhasil dihapus')

def adminChoice(inputStr):
    result = input(f'''
Fitur {inputStr} Buku hanya dapat dilakukan oleh Administrator.
Silahkan masukkan password untuk melanjutkan,
atau masukkan "0" untuk kembali ke menu sebelumnya :
''')
    return result



while(True):
    mainMenu = (input('''
    Selamat datang di perpustakaan. Silahkan pilih menu yang anda inginkan :
    1. Lihat Daftar Buku
    2. Donasi Buku
    3. Pinjam & Edit Buku
    4. Hapus Buku
    5. Meninggalkan Perpustakaan
    '''))

    if mainMenu == '1':
        while(True):
            readMenu = input('''
            Anda dapat melihat seluruh koleksi buku di perpustakaan kami, atau melihat buku sesuai genre yang tersedia
            1. Lihat semua buku
            2. Lihat berdasarkan genre
            3. Kembali ke menu sebelumnya
            ''')

            if readMenu == '1':
                read(books)
            
            elif readMenu == '2':
                if len(books):
                    print('Silahkan pilih dari genre yang tersedia')
                    showGenres(getGenres(books))
                    chooseGenre = int(input()) - 1
                    read(books, chooseGenre)
                else:
                    read(books)

            elif readMenu == '3':
                break


    elif mainMenu == '2':
        while True:
            createMenu = input('''
            Silahkan pilih menu yang anda inginkan. Sebelum mendonasikan buku, anda diminta mengisi formulir terlebih dahulu
            1. Lanjut untuk donasi buku
            2. Kembali ke menu sebelumnya
            ''')

            if createMenu == '1':
                while True:
                    title = input('Masukkan judul buku : ')
                    if checkDuplicate(books, title) == False:
                        genre = input('Masukkan genre buku : ')
                        author = input('Masukkan pengarang buku : ')

                        confirmDonate = input('''
                        Apakah anda yakin ingin mendonasikan buku ini?
                        1. Ya
                        2. Tidak
                        ''')

                        if confirmDonate == '1':
                            create(title, genre, author)
                            print(f'Buku {title} anda telah berhasil didonasikan. Terima kasih atas donasi anda')
                            break
                        elif confirmDonate == '2':
                            break

                    else:
                        print('Maaf, buku yang ingin anda donasikan sudah ada di perpustakaan kami. Saat ini kami hanya menerima buku yang belum kami miliki')
                        break

            elif createMenu == '2':
                break 
    
    elif mainMenu == '3':
        while True:
            updateMenu = input('''
            Silahkan pilih menu yang anda inginkan :
            1. Pinjam Buku
            2. Edit Buku
            3. Kembali ke menu sebelumnya
            ''')

            if updateMenu == '1':
                print('Berikut ini daftar buku-buku yang saat ini tersedia di perpustakaan kami, silahkan pilih salah satu nomor buku :')
                read(books, False, True)
                if len(readAvailable(books)) == 0:
                    continue
                borrowBook = int(input())
                borrow(readAvailable(books), borrowBook)
                break
            
            elif updateMenu == '2':
                while True:
                    inputPassword = adminChoice('Edit')
                    edited = False
                    if inputPassword == '0':
                        break
                    elif inputPassword == adminPassword:
                        print('Silahkan pilih nomor buku yang ingin anda edit : ')
                        read(books)
                        if len(books) == 0:
                            break
                        editBook = int(input())
                        editPart = (input('''
                        Silahkan pilih data yang ingin anda edit
                        1. Edit Judul
                        2. Edit Genre
                        3. Edit Pengarang
                        '''))
                        if editPart == '1':
                            while True:
                                newTitle = input('Silahkan masukkan judul yang baru : ')
                                confirmUpdate = input(f'''
                                Apakah anda yakin ingin mengubah judul buku menjadi {newTitle}?
                                1. Ya
                                2. Tidak
                                ''')
                                if confirm(confirmUpdate):
                                    update(editBook, newTitle)
                                    edited = True
                                    break
                                else:
                                    break
                        elif editPart == '2':
                            while True:
                                newGenre = input('Silahkan masukkan genre yang baru : ')
                                confirmUpdate = input(f'''
                                Apakah anda yakin ingin mengubah genre buku menjadi {newGenre}?
                                1. Ya
                                2. Tidak
                                ''')
                                if confirm(confirmUpdate):
                                    update(editBook, None, newGenre)
                                    edited = True
                                    break
                                else:
                                    break
                        elif editPart == '3':
                            while True:
                                newAuthor = input('Silahkan masukkan pengarang yang baru : ')
                                confirmUpdate = input(f'''
                                Apakah anda yakin ingin mengubah pengarang buku menjadi {newAuthor}?
                                1. Ya
                                2. Tidak
                                ''')
                                if confirm(confirmUpdate):
                                    update(editBook, None, None, newAuthor)
                                    edited = True
                                    break
                                else:
                                    break
                    if edited:
                        break
                    else:
                        print('Password yang anda masukkan salah')

            elif updateMenu == '3':
                break
    
    elif mainMenu == '4':
        while True:
            deleteMenu = input('''
            Silahkan pilih menu yang anda inginkan
            1. Hapus Buku
            2. Kembali ke menu sebelumnya
            ''')
            if deleteMenu == '1':
                inputPassword = adminChoice('Hapus')
                if inputPassword == '0':
                    break
                elif inputPassword == adminPassword:
                    print('Silahkan pilih buku yang ingin anda hapus :\n')
                    read(books)
                    if len(books) == 0:
                        continue
                    deleteBook = int(input())
                    confirmDelete = input(f'''
                    Apakah anda yakin ingin menghapus buku {books[deleteBook-1]['title']}?
                    1. Ya
                    2. Tidak
                    ''')
                    if confirm(confirmDelete):
                        delete(books, deleteBook)
                    else:
                        continue
            elif deleteMenu == '2':
                break

    elif mainMenu == '5':
        print('Terima kasih atas kunjungan anda. Sampai jumpa kembali')
        break

    else:
        print('Mohon masukkan pilihan sesuai menu yang tersedia, yang ditandai dengan angka 1 sampai 5')