from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChatbotSerializer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('SimpleBot')
training_data = [
    "What is the standard maintenance schedule for transformers?",
    "Transformers should undergo a detailed inspection yearly and more comprehensive maintenance every 5 years.",

    "How often should we inspect circuit breakers?",
    "Circuit breakers should be inspected semi-annually and maintained annually.",

    "Are there any specific guidelines for maintaining underground cables?",
    "Underground cables should have visual inspections annually and electrical tests every 3-5 years.",

    "When should battery systems in substations be replaced?",
    "Battery systems typically last 5-7 years, but they should be tested annually for performance.",

    "What are the signs of wear and tear in isolators?",
    "Signs include rusting, physical damage, or malfunctions during operation.",

    "How frequently should we conduct thermal imaging of equipment?",
    "Thermal imaging should be conducted annually or when performance issues arise.",

    "What's the recommended oil testing frequency for transformers?",
    "Transformer oil should be tested annually for dielectric strength and impurities.",

    "How do we detect partial discharge in equipment?",
    "Use specialized partial discharge measurement equipment during routine maintenance checks.",

    "What's the protocol for managing a coolant leak?",
    "Isolate the equipment, contain the leak, and consult the equipment's maintenance manual.",

    "How often should surge arresters be tested?",
    "Surge arresters should be visually inspected annually and electrically tested every 5 years.",

    "What maintenance tasks are required for a gas-insulated substation?",
    "Gas-insulated substations require annual gas quality checks and inspections.",

    "How do we handle corrosion in substation structures?",
    "Check for visible signs of corrosion during routine inspections and repaint or replace corroded parts as necessary.",

    "How often should we inspect grounding systems?",
    "Grounding systems should be visually inspected annually and electrically tested every 3 years.",

    "What's the lifespan of a typical substation transformer?",
    "With proper maintenance, a transformer can last 25-40 years.",

    "How do you recommend cleaning high voltage insulators?",
    "High voltage insulators should be cleaned using non-conductive cleaning solutions and methods.",

    "When should air circuit breakers be lubricated?",
    "Lubricate air circuit breakers annually or as recommended by the manufacturer.",

    "What's the maintenance protocol after a fault event?",
    "After a fault, inspect all equipment involved, test protective relays, and ensure no lasting damage.",

    "How often should we calibrate protective relays?",
    "Protective relays should be calibrated every 2-3 years.",

    "What are the guidelines for vegetation management around substations?",
    "Vegetation should be trimmed to ensure a minimum clearance of 10 feet from all equipment.",

    "Are there any specific maintenance tasks before winter?",
    "Before winter, inspect heating systems, ensure seals are intact, and check for moisture intrusion."
]
trainer = ListTrainer(chatbot)
trainer.train(training_data)

@api_view(['POST'])
def get_response(request):
    user_query = request.data.get('user_query')
    bot_response = chatbot.get_response(user_query)
    serializer = ChatbotSerializer(data={'user_query': user_query, 'bot_response': str(bot_response)})
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)
