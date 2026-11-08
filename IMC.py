# Calculadora de IMC Simples

def calcular_imc():
    print("=== Calculadora de IMC ===")
    
    try:
        # Pede o peso e a altura do usuário
        peso = float(input("Digite o seu peso em kg (ex: 70.5): "))
        altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
        
        # Calcula o IMC
        imc = peso / (altura ** 2)
        
        # Exibe o resultado formatado com 2 casas decimais
        print(f"\nSeu IMC é: {imc:.2f}")
        
        # Classificação do IMC
        if imc < 18.5:
            classificação = "Abaixo do peso"
        elif 18.5 <= imc < 25.0:
            classificação = "Peso normal (saudável)"
        elif 25.0 <= imc < 30.0:
            classificação = "Sobrepeso"
        else:
            classificação = "Obesidade"
            
        print(f"Classificação: {classificação}")
        
    except ValueError:
        print("Por favor, digite apenas números válidos usando ponto (.) para decimais.")

# Executa a função
if __name__ == "__main__":
    calcular_imc()