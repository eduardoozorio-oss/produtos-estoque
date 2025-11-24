from database import get_connection

# Criar produto
def criar_produto(dados):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO produtos (nome, categoria, preco, quantidade)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (
        dados.nome,
        dados.categoria,
        dados.preco,
        dados.quantidade
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Produto cadastrado com sucesso"}

# Listar produtos
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()

    return produtos
from database import get_connection

# Criar produto
def criar_produto(dados):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO produtos (nome, categoria, preco, quantidade)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (
        dados.nome,
        dados.categoria,
        dados.preco,
        dados.quantidade
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Produto cadastrado com sucesso"}

# Listar produtos
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()

    return produtos

# Atualizar produto
def atualizar_produto(id, dados):
    conn = get_connection()
    cursor = conn.cursor()

    if dados.preco is not None:
        cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s",
                       (dados.preco, id))

    if dados.quantidade is not None:
        cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s",
                       (dados.quantidade, id))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Produto atualizado"}


