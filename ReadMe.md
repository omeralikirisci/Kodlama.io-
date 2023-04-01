@pytest.mark.xfail(reason="reason for expected failure") Bu dekoratör, bir test işlevini başarısız olması beklenecek şekilde işaretler ve test gerçekten başarısız olursa test raporunda görüntülenen bir neden sağlar.

@pytest.mark.parametrize("arg1, arg2", [(value1, value2), (value3, value4), ...])Bu dekoratör, bir test işlevinin parametreleştirilmesini sağlayarak birden çok bağımsız değişken kümesiyle çalıştırılmasına izin verir.

@pytest.fixture -Bu dekoratör, birden çok test işlevi arasında paylaşılabilen, yeniden kullanılabilir bir test kodu parçası olan bir fikstür tanımlar. Fikstürler, veritabanı bağlantıları veya geçici dosyalar gibi testin ihtiyaç duyduğu kaynakları kurmak ve ayırmak için kullanılabilir.
@pytest.mark.skip(reason="reason for skipping") Bu dekoratör, test raporunda görüntülenen bir nedenle atlanacak bir test işlevini işaretler.
![Ekran Görüntüsü (56)](https://user-images.githubusercontent.com/104915515/229305650-31d37789-4f43-420f-821e-42e68824613e.png)
