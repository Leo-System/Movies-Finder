import requests

print("""
############################################################
NOTE:To use this program you will need to:

1-Make an acount on rapidapi.com;
2-Subscribe in the api MoviesDatabase(link: https://rapidapi.com/SAdrian/api/moviesdatabase/) on the free plan;
3-Copy your api key from the site to use on this program, the api key will be on the code snippets near "X-RapidAPI-Key".

############################################################
""")

url = "https://moviesdatabase.p.rapidapi.com/titles"

key=input("Insert your api key from RapidAPI.com: ")
ano=int(input("Insert the year of the movies: "))
genero=input("Insert the genre of the movies you want: ")
print("\n")
ano=str(ano)

querystring = {"limit":"50","year":ano,"genre":genero,"titleType":"movie"}
headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

resultados = int(response.json()['entries'])

n=0

print(f"\nNumber of results: {resultados}\n")

while n < resultados:
    nome = response.json()['results'][n]['titleText']['text']
    print(nome)
    n=n+1
