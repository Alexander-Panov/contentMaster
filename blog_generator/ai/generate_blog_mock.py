import asyncio


async def generate_blog_topics_mock(niche, keywords, word_count):
    await asyncio.sleep(3)
    return ['The Role of AI in Enhancing Cybersecurity Measures for Businesses',
            'Exploring Blockchain Technology: Beyond Cryptocurrencies and NFTs',
            'How Machine Learning is Revolutionizing Predictive Analytics in IoT Devices',
            'The Future of Smart Homes: Integrating IoT with AI for Enhanced Living',
            'Cybersecurity Challenges in the Age of Quantum Computing',
            'Ethical Considerations in AI Development: Balancing Innovation and Responsibility',
            'Decentralized Finance (DeFi): Understanding the Impact of Blockchain on Traditional Banking',
            'Harnessing Machine Learning for Real-Time Cyber Threat Detection',
            'The Intersection of AI and IoT: Creating a Seamless User Experience',
            'How Blockchain is Shaping Supply Chain Transparency and Security ',
            'The Importance of Data Privacy in Machine Learning Algorithms ',
            'Innovations in IoT Security: Protecting Your Connected Devices from Attacks ',
            'AI-Powered Chatbots: Transforming Customer Service through Intelligent Automation ',
            'Understanding the Basics of Smart Contracts on Blockchain Platforms ',
            'Emerging Trends in Cybersecurity: What to Expect in the Next Five Years']


async def generate_blog_mock(niche, topic, keywords, word_count):
    await asyncio.sleep(3)
    return """
    In recent years, the plant-based diet has surged in popularity, captivating health enthusiasts and environmental advocates alike. What started as a niche lifestyle choice has transformed into a mainstream movement, with restaurants and supermarkets expanding their offerings to include an array of plant-based options. But what exactly is driving this trend? Is it merely a fad, or does a plant-based diet offer real benefits for our health, nutrition, and the planet? Let’s explore the compelling reasons to embrace this vibrant way of eating.

## Health Benefits: Nourishing Your Body

A plant-based diet is primarily composed of fruits, vegetables, whole grains, nuts, seeds, and legumes while minimizing or eliminating animal products. This dietary shift can lead to numerous health benefits:

### 1. Improved Heart Health
Research consistently shows that individuals who follow a plant-based diet tend to have lower blood pressure and cholesterol levels. The high fiber content from fruits and vegetables helps reduce the risk of heart disease significantly. 

### 2. Weight Management
Plant-based foods are often lower in calories yet high in nutrients, making them ideal for weight management. Studies indicate that those who consume more plant foods tend to maintain healthier body weights compared to meat-eaters.

### 3. Enhanced Digestion
The fiber found in whole plants promotes healthy digestion by supporting regular bowel movements and fostering beneficial gut bacteria. This can lead to reduced risks of gastrointestinal issues such as constipation or diverticulitis.

### 4. Lower Risk of Chronic Diseases
Numerous studies link plant-based diets with reduced risks of chronic diseases like type 2 diabetes and certain types of cancer. The antioxidants present in fruits and vegetables combat inflammation and oxidative stress—key contributors to these illnesses.

## Nutrition: A Nutrient Powerhouse

When done right, a plant-based diet can be exceptionally nutritious:

### Key Nutrients in Plant-Based Foods

- **Fiber**: Essential for digestive health.
- **Vitamins & Minerals**: Fruits and vegetables are rich sources of vitamins A, C, E, K, folate, potassium, and magnesium.
- **Plant-Based Proteins**: Beans, lentils, quinoa, tofu, tempeh—these are fantastic sources that help meet daily protein needs without relying on animal products.

### Balancing Nutritional Needs
While adopting a plant-based diet offers many advantages, it's crucial to ensure you’re meeting all your nutritional needs:

- **Vitamin B12**: Generally found in animal products; consider fortified foods or supplements.
- **Iron**: Plant sources like lentils and spinach provide iron but may require pairing with vitamin C-rich foods for better absorption.
- **Omega-3 Fatty Acids**: Found in flaxseeds and chia seeds; consider incorporating these into your meals for heart health.

## Sustainability: Caring for Our Planet

One of the most compelling reasons to adopt a plant-based diet is its positive impact on the environment:

### Reduced Carbon Footprint
Animal agriculture is responsible for significant greenhouse gas emissions; transitioning towards a more plant-centric diet can reduce an individual’s carbon footprint dramatically.

### Conservation of Resources
Producing plants typically requires less land and water than raising livestock:
- Producing one pound of beef requires about 1,800 gallons of water compared to just 39 gallons for one pound of beans.
  
### Biodiversity Preservation
By shifting away from meat-heavy diets that often contribute to deforestation (for grazing lands), we help protect wildlife habitats and promote biodiversity.

## Delicious Plant-Based Recipes

Transitioning to a plant-based lifestyle doesn’t mean sacrificing flavor! Here are three easy recipes that showcase how delicious this way of eating can be:

### 1. Quinoa Salad Bowl 
Ingredients:
- Cooked quinoa 
- Chopped cucumbers 
- Cherry tomatoes 
- Avocado 
- Lemon vinaigrette 

Instructions:
1. In a large bowl combine cooked quinoa with chopped veggies.
2. Drizzle lemon vinaigrette over the top before serving.

### 2. Lentil Tacos 
Ingredients:
- Cooked lentils 
- Taco seasoning 
- Corn tortillas 
- Lettuce & avocado 

Instructions:
1. Heat lentils with taco seasoning.
2. Serve in corn tortillas topped with lettuce and avocado slices.

### 3. Chickpea Curry 
Ingredients:
- Canned chickpeas 
- Coconut milk 
- Curry powder 
- Spinach 

Instructions:
1. In a pan over medium heat combine chickpeas with coconut milk and curry powder.
2. Add spinach until wilted; serve over rice!

## Conclusion: Embrace the Change!

Adopting a plant-based diet not only nourishes your body but also promotes sustainability and environmental responsibility—a win-win situation! By integrating more whole foods into your meals while being mindful about nutrition balance—your journey toward better health can be both fulfilling and delicious.

Are you ready to take the plunge into a world brimming with vibrant flavors? Or perhaps you’re already on this journey—what challenges or triumphs have you experienced along the way? Share your thoughts below!
    """.strip()
