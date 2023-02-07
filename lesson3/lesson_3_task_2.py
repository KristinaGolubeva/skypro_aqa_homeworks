from smartphone import Smartphone

Xiaomi=Smartphone('Xiaomi', 'Poco X3', "+79113452635")
Huawei=Smartphone('Huawei', 'Honor 6', "+79215674453")
Google=Smartphone('Google', 'Pixel 7', "+79645679800")
Samsung=Smartphone('Samsung', 'Galaxy S22', "+79115554678")
Nokia=Smartphone('Nokia', 'X30', "+77776589967")

catalog=[Xiaomi, Huawei, Google, Samsung, Nokia]

for i in catalog:
    i.Say()