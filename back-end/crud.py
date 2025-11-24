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

