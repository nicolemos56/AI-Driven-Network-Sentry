import google.generativeai as genai
import os
import json
import re

class AIAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    async def analyze_and_decide(self, telemetry):
        prompt = f"""
        Você é o AGENTE SENTINELA v3. Analise esta telemetria real:
        {telemetry}

        REGRAS:
        1. Se 'network' é DOWN, o dispositivo está sem link ou energia. Risco: MEDIUM. Ação: RESET APN.
        2. Se 'network' é UP mas 'portal' é DOWN, falha de software. Risco: LOW. Ação: CONFIG RELOAD.
        3. Se 'unknown' for true, ignore regras acima. Risco: HIGH. Ação: MANUAL INTERVENTION.

        Retorne APENAS um JSON:
        {{
            "risk_level": "LOW" | "MEDIUM" | "HIGH",
            "diagnosis": "diagnóstico curto",
            "suggested_action": "acao",
            "reasoning": "sua lógica baseada nos números",
            "requires_approval": true | false
        }}
        """
        try:
            response = self.model.generate_content(prompt)
            # Limpeza robusta de JSON
            clean_json = re.search(r'\{.*\}', response.text, re.DOTALL).group()
            return json.loads(clean_json)
        except Exception as e:
            return {
                "risk_level": "HIGH",
                "diagnosis": "Erro de Processamento Cognitivo",
                "suggested_action": "REBOOT",
                "reasoning": f"Falha na API de IA: {str(e)}",
                "requires_approval": True
            }