import streamlit as st

def inicializar_banco():
    """Conecta ao Neon e cria a tabela 'carros' se ela não existir."""
    try:
        # Usa o conector nativo de SQL do Streamlit puxando os secrets automaticamente
        conn = st.connection("postgres", type="sql", url=st.secrets["postgres"]["url"])
        
        # Executa o comando SQL de criação de tabela
        with conn.session as session:
            session.execute("""
                CREATE TABLE IF NOT EXISTS carros (
                    id SERIAL PRIMARY KEY,
                    carro VARCHAR(100) NOT NULL,
                    ano INT NOT NULL,
                    cambio VARCHAR(50) NOT NULL
                );
            """)
            session.commit()
    except Exception as e:
        st.error(f"Erro ao inicializar o banco de dados: {e}")
