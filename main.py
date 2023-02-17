from vkaudiotoken import get_kate_token, get_vk_official_token

login = '+79500216197' # your vk login, e-mail or phone number
password = 'Rabota_23' # your vk password

# print tokens and corresponding user-agent headers
print(get_kate_token(login, password))
print(get_vk_official_token(login, password))
