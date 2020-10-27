from selenium import webdriver
import time

PATH = "/home/brunaostii/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/index")

link = driver.find_element_by_link_text("Cadastrar clientes")
link.click()

nome = driver.find_element_by_name("nome")
telefone = driver.find_element_by_name("telefone")
cpf = driver.find_element_by_name("cpf")
email = driver.find_element_by_name("email")

nome.send_keys("Bruna")
telefone.send_keys("2115452")
cpf.send_keys("342645376585")
email.send_keys("bruna@hotmail.com")

cadastro = driver.find_element_by_name("submit")
cadastro.click()

listar = driver.find_element_by_link_text("Lista de clientes")
listar.click()

excluir = driver.find_elements_by_link_text("X")[0].click()
atualizar = driver.find_elements_by_link_text("o")[0].click()

nome = driver.find_element_by_name("nome")
telefone = driver.find_element_by_name("telefone")
cpf = driver.find_element_by_name("cpf")
email = driver.find_element_by_name("email")

nome.clear()
telefone.clear()
cpf.clear()
email.clear()

nome.send_keys("Bruna ATUALIZADO")
telefone.send_keys("555555555")
cpf.send_keys("9999999999")
email.send_keys("atualizado@hotmail.com")

cadastro = driver.find_element_by_name("submit")
cadastro.click()




