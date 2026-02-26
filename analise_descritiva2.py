import pandas as pd
import holidays

# Criamos a lista de feriados do Brasil (pode especificar o estado, ex: state='SP')
feriados_br = holidays.Brazil()
mood_map = {
    # ENERGIA LÁ NO ALTO / TREINO / AGRESSIVO
    'nu metal': 'Agitado', 'thrash metal': 'Agitado', 'metal': 'Agitado', 'hard rock': 'Agitado',
    'power metal': 'Agitado', 'heavy metal': 'Agitado', 'glam metal': 'Agitado', 'groove metal': 'Agitado',
    'alternative metal': 'Agitado', 'rap metal': 'Agitado', 'industrial rock': 'Agitado', 'punk': 'Agitado',
    'horror punk': 'Agitado', 'egg punk': 'Agitado', 'skate punk': 'Agitado', 'grunge': 'Agitado',
    'post-grunge': 'Agitado', 'emo': 'Agitado', 'midwest emo': 'Agitado', 'queercore': 'Agitado',
    'rage rap': 'Agitado', 'drum and bass': 'Agitado', 'dubstep': 'Agitado', 'breakcore': 'Agitado',

    # FOCO / TRABALHO PROFUNDO / INSTRUMENTAL
    'video game ost': 'Foco', 'video game music': 'Foco', 'japanese vgm': 'Foco', 'soundtrack': 'Foco',
    'orchestral': 'Foco', 'piano': 'Foco', 'ambient': 'Foco', 'downtempo': 'Foco', 'lo-fi': 'Foco',
    'instrumental': 'Foco', 'post-rock': 'Foco', 'idm': 'Foco', 'liquid funk': 'Foco', 'lo-fi house': 'Foco',

    # FESTA / AGITO / DANÇANTE
    'edm': 'Festa', 'electronic': 'Festa', 'electropop': 'Festa', 'house': 'Festa', 'tech house': 'Festa',
    'deep house': 'Festa', 'future house': 'Festa', 'tropical house': 'Festa', 'electro house': 'Festa',
    'disco house': 'Festa', 'nu disco': 'Festa', 'euroswing': 'Festa', 'electro swing': 'Festa', 'techno': 'Festa',
    'dance': 'Festa', 'hyperpop': 'Festa', 'nightcore': 'Festa', 'brazilian funk': 'Festa', 'funk': 'Festa',
    'axé': 'Festa', 'piseiro': 'Festa', 'reggaeton': 'Festa', 'neoperreo': 'Festa', 'trap latino': 'Festa',

    # SOCIAL / RELAXAR / DESCONTRAÇÃO
    'pop': 'Relax / Social', 'brazilian pop': 'Relax / Social', 'indie pop': 'Relax / Social', 'synthpop': 'Relax / Social',
    'soft pop': 'Relax / Social', 'korean': 'Relax / Social', 'j-pop': 'Relax / Social', 'mpb': 'Relax / Social',
    'new mpb': 'Relax / Social', 'pagode': 'Relax / Social', 'pagode baiano': 'Relax / Social', 'samba': 'Relax / Social',
    'sertanejo': 'Relax / Social', 'forró': 'Relax / Social', 'reggae': 'Relax / Social', 'lo-fi house': 'Relax / Social',
    'bedroom pop': 'Relax / Social', 'rnb': 'Relax / Social', 'alternative r&b': 'Relax / Social',

    # INTROSPECTIVO / INDIE / REFLEXIVO
    'indie': 'INDIE', 'indie rock': 'INDIE', 'alternative rock': 'INDIE', 'art rock': 'INDIE',
    'art pop': 'INDIE', 'dream pop': 'INDIE', 'shoegaze': 'INDIE', 'folk': 'INDIE',
    'folk pop': 'INDIE', 'singer-songwriter': 'INDIE', 'acoustic': 'INDIE', 'blues': 'INDIE',
    'acid jazz': 'INDIE', 'jazz': 'INDIE', 'nu jazz': 'INDIE', 'trip hop': 'INDIE',

    # URBANO / ESTILO / RAP
    'hip hop': 'Urbano', 'rap': 'Urbano', 'brazilian trap': 'Urbano', 'brazilian hip hop': 'Urbano', 'trap': 'Urbano',
    'grime': 'Urbano', 'underground hip hop': 'Urbano', 'experimental hip hop': 'Urbano', 'jazz rap': 'Urbano',
    'anime rap': 'Urbano', 'french rap': 'Urbano', 'melodic rap': 'Urbano',

    # CLÁSSICO / NOSTALGIA / RETRÔ
    'classic rock': 'Nostálgico', 'rock': 'Nostálgico', 'brazilian rock': 'Nostálgico', 'progressive rock': 'Nostálgico',
    'blues rock': 'Nostálgico', 'glam rock': 'Nostálgico', 'soft rock': 'Nostálgico', '80s': 'Nostálgico', 'new wave': 'Nostálgico',
    'disco': 'Nostálgico', 'retro soul': 'Nostálgico', 'soul': 'Nostálgico'
}


def definir_periodo(hora):
    if 5 <= hora < 12:
        return 'Manhã'
    elif 12 <= hora < 18:
        return 'Tarde'
    elif 18 <= hora < 24:
        return 'Noite'
    else:
        return 'Madrugada'

# Criamos uma função para checar se é dia útil de verdade
def checar_dia_util_real(data):
    # Se for Sábado (5) ou Domingo (6) OU estiver na lista de feriados
    if data.weekday() >= 5 or data in feriados_br:
        return 'Não Útil'
    return 'Útil'


def pegar_top_3_moods(lista_generos):
    # 1. Pega os 3 gêneros mais frequentes naquela hora/dia
    top_3_generos = lista_generos.value_counts().nlargest(3).index.tolist()
    
    # 2. Mapeia para os Moods (usando o seu mood_map)
    # Usamos dict.get(g, g) para que se o gênero não estiver no mapa, ele mostre o nome do gênero
    moods = [mood_map.get(g.lower(), 'Outros') for g in top_3_generos]
    
    # Retorna a lista (ou uma string formatada se preferir ver direto na tabela)
    return moods

def tratar_dia_semana(dia):
    """
    Recebe um valor representando um dia da semana e retorna
    o nome padronizado no formato 'segunda-feira'.
    Retorna None se for inválido.
    """

    if not isinstance(dia, str) and not isinstance(dia, int):
        return None

    # Dicionário de normalização
    dias = {
        1: "Segunda",
        2: "Terça",
        3: "Quarta",
        4: "Quinta",
        5: "Sexta",
        6: "Sábado",
        7: "Domingo"
    }

    apelidos = {
        "seg": 1, "segunda": 1, "segunda-feira": 1,
        "ter": 2, "terça": 2, "terca": 2, "terça-feira": 2, "terca-feira": 2,
        "qua": 3, "quarta": 3, "quarta-feira": 3,
        "qui": 4, "quinta": 4, "quinta-feira": 4,
        "sex": 5, "sexta": 5, "sexta-feira": 5,
        "sab": 6, "sábado": 6, "sabado": 6,
        "dom": 7, "domingo": 7
    }

    # Se for número
    if isinstance(dia, int):
        return dias.get(dia)

    # Se for string
    dia_tratado = dia.strip().lower()

    # Se for número em string
    if dia_tratado.isdigit():
        return dias.get(int(dia_tratado))

    numero_dia = apelidos.get(dia_tratado)

    if numero_dia:
        return dias[numero_dia]

    return None

def tratar_periodo(periodo):
    """
    Recebe um valor representando um período e retorna
    o nome padronizado
    Retorna None se for inválido.
    """
    # Dicionário de normalização
    periodos = {
        1: "Manhã",
        2: "Tarde",
        3: "Noite",
        4: "Madrugada"
    }

    apelidos = {
        "manhã": 1, "manha": 1,"anha": 1,"anhã": 1, "mnha": 1,"mnhã": 1, "maha": 1 , "mahã": 1, "mana": 1,"manã": 1, "manh": 1,
        "tarde": 2, "arde": 2, "trde": 2, "tade": 2, "tare": 2, "tard": 2,
        "noite": 3, "oite": 3, "nite": 3, "note": 3, "noie": 3, "noit": 3,
        "madrugada": 4, "adrugada": 4, "mdrugada": 4, "marugada": 4, "madugada": 4, "madrgada": 4, "madruada": 4, "madrugda": 4, "madrugaa": 4, "madrugad": 4
    }

   
    # Se for string
    periodo_tratado = periodo.strip().lower()

    numero_periodo = apelidos.get(periodo_tratado)

    if numero_periodo:
        return periodos[numero_periodo]

    return None



def calcular_mood_simples(dia_escolhido, periodo_escolhido, tabela_top_3, df):
    # 1. Filtrar as horas que pertencem àquele período E que existem no dia escolhido
    # Filtramos o DF original para garantir que pegamos horas que tiveram reprodução
    horas_periodo = df[(df['periodo'] == periodo_escolhido) & (df['dia'] == dia_escolhido)]['hora'].unique()
    
    pontuacao_moods = {}

    for hora in horas_periodo:
        if hora in tabela_top_3.index:
            lista_moods = tabela_top_3.loc[hora, dia_escolhido]
            
            # VERIFICAÇÃO: Só tenta iterar se for uma lista (e não NaN/float)
            if isinstance(lista_moods, list):
                # 2. Atribuir pontos baseados na posição (Ponderação)
                for i, mood in enumerate(lista_moods):
                    pontos = 3 - i  # 1º lugar = 3pts, 2º = 2pts, 3º = 1pt
                    pontuacao_moods[mood] = pontuacao_moods.get(mood, 0) + pontos

    # 3. Caso o período esteja vazio (usuário não ouviu nada nessa hora/dia)
    if not pontuacao_moods:
        return "Silêncio...", {}

    # 4. Ordenar pelos pontos e pegar o vencedor
    vencedor = max(pontuacao_moods, key=pontuacao_moods.get)
    return vencedor, pontuacao_moods


def menu():

    rodando = True
    while rodando:

        print("--- 🎵 Análise de Mood Spotify 🎵 ---")
        dia = input("Escolha um dia (ex: Segunda): ")
        dia = tratar_dia_semana(dia)
        
        if dia == None:
            print("❌ Dia digitado incorretamente! Tente novamente.")
            continue


        print("1 - Mood Simples (Resumo do Período)\n2 - Mood Específico (Hora Exata)")
        tipo = input("Opção: ")

        if tipo == '1':
            per = input("Qual período? (Manhã/Tarde/Noite/Madrugada): ")
            per = tratar_periodo(per)
            if per == None:
                print("❌ Período digitado incorretamente! Tente novamente.")
                continue

            vencedor, scores = calcular_mood_simples(dia, per, tabela_top_3, df)            
            emoji_map = {
                'Agitado': '⚡', 'Foco': '🧠', 'Fesya': '🎉', 
                'Social / Relax': '🍃', 'Introspectivo': '☕', 'Urbano': '🏙️'
            }
            emo = emoji_map.get(vencedor, '🎵')

            mensagem_saida = ""

            if dia == 'Sábado' or dia == 'Domingo':
                mensagem_saida += "No " + str (dia)
            else: 
                mensagem_saida += "Na " + str (dia)

            if per == 'Tarde' or per == 'Noite':
                mensagem_saida += " à " + str(per) + f", seu mood predominante é: {emo} {vencedor}"
            else:
                mensagem_saida += " de " + str(per) + f", seu mood predominante é: {emo} {vencedor}"

            print("\n✨ "+ mensagem_saida)

            mensagem = ' Ranking de força no período: '
            for mood, ponto in scores.items():
                mensagem += "\n" + mood + " - " + str(ponto)

            if scores:
                print(mensagem)    
            
        elif tipo == '2':
            try:
                hora = int(input("Qual hora? (0-23): "))
                if hora in tabela_top_3.index:
                    lista = tabela_top_3.loc[hora, dia]
                    
                    if isinstance(lista, list):
                        print(f"\n🔍 Raio-X das {hora}h no(a) {dia}:")
                        for index, posicao in enumerate(lista):
                            print(f"{index+1}º Lugar: {posicao}")
                    else:
                        print(f"\n:🚨 Sem dados suficientes para às {hora}h de {dia}.")
                else:
                    print("\n🚨Hora não encontrada na base de dados.")
            except ValueError:
                print("\n❌ Por favor, digite um número válido para a hora.")
        else:
            print("❌ Opa, não existe esse mood! Por favor digitar 1 ou 2 na próxima.")
            continue

        print("-" * 30)
        opcao_saida = input("Deseja continuar? (sim/nao): ").strip().lower()
        if opcao_saida == 'nao' or opcao_saida == 'não':
            print("\nEncerrando o sistema... Até a próxima!")
            rodando = False


df = pd.read_csv("spotify_songs_bahia.csv", delimiter=",")

df['ts'] = pd.to_datetime(df['ts'])

# Mapeamento para traduzir (opcional, se o seu sistema estiver em inglês)
dias_pt = {
    'Monday': 'Segunda', 'Tuesday': 'Terça', 'Wednesday': 'Quarta',
    'Thursday': 'Quinta', 'Friday': 'Sexta', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
}

df['dia'] = df['ts'].dt.day_name().map(dias_pt)

# Extrai a hora e aplica a função
df['periodo'] = df['ts'].dt.hour.apply(definir_periodo)

df['status_dia'] = df['ts'].apply(checar_dia_util_real)
df['hora'] = df['ts'].dt.hour

# Aplicando o agrupamento
mood_sequencial = df.groupby(['dia', 'hora'])['genero'].agg(pegar_top_3_moods).reset_index()

# Pivotando
tabela_top_3 = mood_sequencial.pivot(index='hora', columns='dia', values='genero')

# Reordenando os dias para ficar intuitivo
ordem_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
tabela_top_3 = tabela_top_3.reindex(columns=ordem_dias)

# Exibindo o resultado
print(tabela_top_3)

menu()


