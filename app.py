from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    artworks = [
        {
            "title": "THE GRAVITY BETWEEN US",
            "image": "images/THE GRAVITY BETWEEN US.jpg",
            "poem": "poems/THE GRAVITY BETWEEN US P.jpg",
            "description": "Two souls float in opposite worlds, one burning, one hollow  reaching for each other but never touching."
        },
        {
            "title": "BIRTH",
            "image": "images/BIRTH.jpg",
            "poem": "poems/BIRTH P.jpg",
            "description": "Birth marks the profound beginning of existence—a journey defined by growth, transformation, and endless possibility. This piece celebrates the miracle of life, capturing the innocence and hope that accompany every new chapter. It serves as a powerful reminder that within each of us lies the potential for greatness, and that every soul is deserving of love, support, and the chance to flourish."
        },
        {
            "title": "CALL YOURSELF IF YOU GET LOST",
            "image": "images/CALL YOURSELF IF YOU GET LOST.jpg",
            "poem": "poems/CALL YOURSELF IF YOU GET LOST P.jpg",
            "description": "This artwork invites viewers into a surreal, dreamlike city built from the architecture of thoughts and memories. It explores the profound solitude that often accompanies self-discovery, encouraging deep reflection and resilience in the face of uncertainty. Through winding alleys and shifting landscapes, the piece suggests that even when we feel lost, we can find strength and clarity by reconnecting with our inner selves."
        },
        {
            "title": "FUJI 5K (DEATH IS A TRADEMARK)",
            "image": "images/FUJI 5K (DEATH IS A TRADEMARK).jpg",
            "poem": "poems/FUJI 5K (DEATH IS A TRADEMARK) P.jpg",
            "description": "A raw, symbolic meditation on mortality and the shifting nature of identity, this piece fuses chaotic visuals with poetic undertones to challenge the boundaries of reality. It confronts the inevitability of death, questioning what it means to leave a mark on the world. Through its layered imagery, the artwork invites viewers to reflect on the trademarks we leave behind and the ways in which chaos and order shape our existence."
        },
        {
            "title": "FACES OF LIFE",
            "image": "images/FACES OF LIFE.jpg",
            "poem": "poems/FACES OF LIFE P.jpg",
            "description": "This evocative piece delves into the many faces we wear throughout our lives, exploring themes of self-reflection, nostalgia, and personal growth. It contemplates the choices we wish we had made in our youth and the lessons learned along the way. Ultimately, it is a celebration of living in the present, embracing who we are, and envisioning who we might become as we continue to evolve."
        },
        {
            "title": "CORRUPTION",
            "image": "images/CORRUPTION.jpg",
            "poem": "poems/CORRUPTION P.jpg",
            "description": "Corruption examines the seductive nature of power and the fragile line between integrity and moral compromise. Through stark contrasts and symbolic imagery, the artwork reveals how easily virtue can be overshadowed by ambition. It serves as a cautionary tale, reminding us that every individual harbors the capacity for both good and evil, and that true strength lies in choosing integrity over corruption."
        },
        {
            "title": "THE END",
            "image": "images/THE END.jpg",
            "poem": "poems/THE END P.jpg",
            "description": "This piece captures the bittersweet moment when one chapter closes and another begins. It reflects on the cyclical nature of life, where every ending is also a new beginning. Through its contemplative mood, the artwork encourages viewers to embrace change, honor the past, and step forward with hope into the unknown future."
        },
        {
            "title": "REGRET",
            "image": "images/REGRET.jpg",
            "poem": "poems/REGRET P.jpg",
            "description": "Regret is a haunting exploration of the wounds left by missed opportunities and unspoken words. The piece weaves together memories and hindsight, illustrating how our choices—both made and unmade—shape the fabric of our lives. It evokes the lingering presence of what might have been, urging viewers to confront the silent ache of regret and find meaning in the lessons it imparts."
        },
         {
            "title": "I AM ART",
            "image": "images/I AM ART.jpg",
            "poem": "poems/I AM ART P.jpg",
            "description": "I AM ART challenges viewers to see beyond superficial appearances, delving into the raw, untamed realities that art can reveal. The piece asserts that true artistry lies in vulnerability and authenticity, inviting us to embrace the beauty found in imperfection. It is a bold declaration of the transformative power of creative expression."
        },
        {
            "title": "CHASM",
            "image": "images/CHASM.jpg",
            "poem": "poems/CHASM P.jpg",
            "description": "Chasm delves into the often unseen battles waged within the mind, shining a light on the internal struggles associated with mental health. Through its evocative imagery, the piece seeks to bridge the gap between isolation and understanding, encouraging empathy and compassion for those navigating the depths of their own chasms."
        },
        {
            "title": "DOULEUR",
            "image": "images/DOULEUR.jpg",
            "poem": "poems/DOULEUR P.jpg",
            "description": "Douleur is a poignant meditation on the intertwined pains of love, loss, and regret. The artwork captures the intensity of human emotion, illustrating how heartache can both wound and transform us. Through its expressive forms, the piece invites viewers to reflect on the resilience that emerges from suffering and the hope that can be found in healing."
        },
        {
            "title": "FACELESS ODYSSEY",
            "image": "images/FACELESS ODYSSEY.jpg",
            "poem": "poems/FACELESS ODYSSEY P.jpg",
            "description": "Faceless Odyssey embarks on a journey through the shifting landscapes of identity and self-discovery. The piece explores the challenges of defining oneself in a world of constant change, highlighting the courage required to seek authenticity. It is a tribute to the odyssey each of us undertakes in pursuit of meaning and belonging."
        },
        {
            "title": "DOGS EAT DOGS",
            "image": "images/DOGS EAT DOGS.jpg",
            "poem": "poems/DOGS EAT DOGS P.jpg",
            "description": "Dogs Eat Dogs confronts the harsh realities of violence, selfishness, and self-destruction that can pervade human society. Through its raw and unflinching imagery, the artwork exposes the destructive cycles that perpetuate suffering. It serves as a call to break free from these patterns and seek a more compassionate, harmonious existence."
        },
        {
            "title": "ISOLATION",
            "image": "images/ISOLATION.jpg",
            "poem": "poems/ISOLATION P.jpg",
            "description": "Isolation delves into the profound sense of separation that can affect the human condition, spirit, and mind. The piece captures the loneliness that often accompanies introspection, while also suggesting the possibility of connection and understanding. It is a meditation on the universal experience of isolation and the hope for reconnection."
        },
        {
            "title": "FOLASHADE MIZUKI",
            "image": "images/FOLASHADE MIZUKI.jpg",
            "poem": "poems/FOLASHADE MIZUKI P.jpg",
            "description": "Folashade Mizuki is a striking fusion of tradition and futurism, weaving together the timeless values of honor, sacrifice, and legacy with a visionary narrative. Drawing inspiration from Japanese bushido, the piece follows a solitary warrior as they navigate a world shaped by both ancient codes and futuristic challenges. The accompanying poem deepens the story, reflecting on themes of loss, resilience, and the enduring quest for meaning in a changing world."
        },
        {
            "title": "REBIRTH OF VISION",
            "image": "images/REBIRTH OF VISION.jpg",
            "poem": "poems/REBIRTH OF VISION P.jpg",
            "description": "Rebirth of Vision celebrates the transformative power of renewal, focusing on the rebirth of both spirit and mind. The artwork captures the moment of awakening, when old limitations fall away and new possibilities emerge. It is an ode to the resilience of the human soul and the endless capacity for growth and reinvention."
        },
        {
            "title": "MOTION MADE US",
            "image": "images/MOTION MADE US.jpg",
            "poem": "poems/MOTION MADE US P.jpg",
            "description": "Motion Made Us is a dynamic exploration of the journeys we undertake together, highlighting the strength found in unity and shared ambition. The piece pulses with rhythm and movement, reflecting the interconnectedness of human experience. It is a celebration of resilience, collaboration, and the unstoppable force of collective progress."
        },
        {
            "title": "INTO THE ABYSS, I WONDERED",
            "image": "images/INTO THE ABYSS, I WONDERED.jpg",
            "poem": "poems/INTO THE ABYSS, I WONDERED P.jpg",
            "description": "Into the Abyss, I Wondered captures the moment of transition between endings and new beginnings. The artwork evokes the uncertainty and curiosity that accompany stepping into the unknown, encouraging viewers to embrace the mysteries that lie ahead. It is a meditation on courage, transformation, and the endless cycle of journeys."
        },
        {
            "title": "HEAVEN,HELL AND I",
            "image": "images/HEAVEN,HELL AND I.jpg",
            "poem": "poems/HEAVEN,HELL AND I P.jpg",
            "description": "Heaven, Hell and I delves into the profound internal struggle between light and darkness, good and evil, that defines the human experience. The piece explores the duality of our nature, capturing the tension between opposing forces within the self. Through its evocative imagery, it invites viewers to reflect on the journey toward self-understanding and the quest for balance amidst inner conflict."
        },
        {
            "title": "SAVE YOUR SOUL",
            "image": "images/SAVE YOUR SOUL.jpg",
            "poem": "poems/SAVE YOUR SOUL P.jpg",
            "description": "Save Your Soul is a powerful exploration of self-redemption and the journey to discover one's true essence. The piece delves into the transformative process of shedding false identities and embracing authenticity. Through its evocative imagery, it captures the moment of realization when one chooses to break free from self-imposed limitations and societal expectations. It is a testament to the courage required to confront one's inner demons and emerge stronger, more authentic, and truly alive."
        },
        {
            "title": "MEET THE GALAGHERS",
            "image": "images/MEET THE GALAGHERS.jpg",
            "poem": "poems/MEET THE GALAGHERS P.jpg",
            "description": "Meet the Galaghers is a poignant exploration of the complexities of family relationships, highlighting the challenges and joys of navigating the dynamics of love and connection. The piece delves into the intricacies of human relationships, capturing the nuances of trust, forgiveness, and the unbreakable bond of family. Through its evocative imagery, it invites viewers to reflect on the importance of understanding and accepting one another's imperfections, ultimately finding solace and strength in the unconditional love of family."
        },
        {
            "title": "DONT GO TO REHAB BABY, YOU'RE SO MUCH FUN",
            "image": "images/DONT GO TO REHAB BABY, YOU'RE SO MUCH FUN.jpg",
            "poem": "poems/DONT GO TO REHAB BABY, YOU'RE SO MUCH FUN P.jpg",
            "description": "Don't Go to Rehab Baby, You're So Much Fun is a poignant exploration of addiction and its impact on personal relationships. The piece delves into the complexities of addiction, capturing the destructive cycle it can create. Through its evocative imagery, it invites viewers to reflect on the importance of seeking help and finding support in overcoming addiction, ultimately leading to a path of recovery and healing."
        },
        {
            "title": "UNEASY LIES THE HEAD THAT WEARS THE CROWN",
            "image": "images/UNEASY LIES THE HEAD THAT WEARS THE CROWN.jpg",
            "poem": "poems/UNEASY LIES THE HEAD THAT WEARS THE CROWN P.jpg",
            "description": "Uneasy Lies the Head That Wears the Crown is an exploration of the complexities of power and the weight of responsibility that comes with it."
        },
        {
            "title": "UNTITLED I",
            "image": "images/UNTITLED I.jpg",
        },
        {
            "title": "UNTITLED II",
            "image": "images/UNTITLED II.jpg",
        },
        {
            "title": "UNPLUGGED FROM PERFECTION",
            "image": "images/UNPLUGGED FROM PERFECTION.jpg",
            "poem": "poems/UNPLUGGED FROM PERFECTION P.jpg",
            "description": "Unplugged from Perfection is a powerful meditation on the importance of trusting your own truth in a world of illusions and facades. The piece challenges viewers to look beyond surface appearances and question the authenticity of what they see. Through its striking imagery, it exposes the masks people wear and the pressure to conform to societal expectations. It serves as a reminder to stay true to your inner voice, resist external pressures, and trust your own judgment when others may be presenting false versions of themselves. The artwork encourages us to unplug from the artificial standards of perfection and embrace the courage to see and speak our own truth."
        },
        {
            "title": "ROOTED IN RHYTHM",
            "image": "images/ROOTED IN RHYTHM.jpg",
            "poem": "poems/ROOTED IN RHYTHM P.jpg",
            "description": "rooted in rhythm, wrapped in love. Old school love still hits different"},
        {
            "title": "THE FUTURE  A SNEAK PEEK",
            "image": "images/THE FUTURE  A SNEAK PEEK.jpg",
            "poem": "poems/THE FUTURE  A SNEAK PEEK P.jpg",
            "description": "The Future  A Sneak Peek is a powerful exploration of the importance of looking beyond the present moment and envisioning a brighter future. The piece delves into the complexities of identity and the need to break free from societal expectations. Through its evocative imagery, it invites viewers to reflect on the importance of authenticity and the power of self-expression."
        },
        
        {
            "title": "YOU CANT HAVE YOUR CAKE AND EAT IT TOO",
            "image": "images/YOU CANT HAVE YOUR CAKE AND EAT IT TOO.jpg",
            "poem": "poems/YOU CANT HAVE YOUR CAKE AND EAT IT TOO P.jpg",
            "description": "You Can't Have Your Cake and Eat It Too is a artwork of the complexities of power and the weight of responsibility that comes with it."
        },
        {
            "title": "WITHIN YOUR SIGHT",
            "image": "images/WITHIN YOUR SIGHT.jpg",
            "poem": "poems/WITHIN YOUR SIGHT P.jpg",
            "description": "Within Your Sight is a powerful exploration of the importance of looking beyond the present moment."
        },
        {
            "title": "WINDOWS TO THE SOUL", 
            "image": "images/WINDOWS TO THE SOUL.jpg",
            "poem": "poems/WINDOWS TO THE SOUL P.jpg",
            "description": "Windows to the Soul is an evocative ink drawing that captures an intimate moment between two faces, their profiles nearly touching in a tender, almost melancholic embrace. Rendered with fine, cross-hatched lines, the artwork emphasizes the eyes—wide, expressive, and heavy with emotion—serving as the titular 'windows' to unspoken feelings."
        },
        {
            "title": "YOU WERE NEVER INVITED",
            "image": "images/YOU WERE NEVER INVITED.jpg",
            "poem": "poems/YOU WERE NEVER INVITED P.jpg",
            "description": "The black-and-white illustration, with its chaotic, distorted faces and figures surrounding a single red heart, likely symbolizes emotional turmoil, societal pressure, or inner conflict. The stark contrast of the monochromatic palette with the red heart at the center suggests a focal point of raw emotion—perhaps love, pain, or vulnerability—struggling to stand out amidst overwhelming chaos."
        },
        {
            "title": "WETIN MY EYES NEVER SEE",
            "image": "images/WETIN MY EYES NEVER SEE.jpg",
            "poem": "poems/WETIN MY EYES NEVER SEE P.jpg",
            "description": "A haunting pen and ink portrait capturing the emotional weight of exhaustion and disillusionment. With hollow eyes and expressive hands painted in stark red and black nails, the artwork evokes a deep sense of weariness—an intimate reflection on enduring hardship and unseen struggles."
        },
        {
            "title": "WHISPERS OF FORGOTTEN TIME",
            "image": "images/WHISPERS OF FORGOTTEN TIME.jpg",
            "poem": "poems/WHISPERS OF FORGOTTEN TIME P.jpg",
            "description": "A somber, contemplative piece rendered in dense ink lines, this artwork portrays a figure with closed eyes and clenched hands, immersed in silent reflection. The overlapping forms and heavy shadows suggest a quiet struggle with memory—echoes of a past long buried but not gone. A visual poem of solitude, introspection, and the weight of time."
        },
        {
            "title": "THE MOUTH THAT SWALLOWS SILENCE",
            "image": "images/THE MOUTH THAT SWALLOWS SILENCE.jpg",
            "poem": "poems/THE MOUTH THAT SWALLOWS SILENCE P.jpg",
            "description": "A striking graphite sketch of a face with fingers in the mouth, symbolizing self-censorship, paired with a poem exploring suppressed speech and inner conflict. This work reflects contemporary struggles with expression and mental health, blending visual and textual art to provoke deep reflection."
        },
        # ... Add all artworks like this
    ]
    return render_template("index.html", artworks=artworks)
    
if __name__ == "__main__":
    app.run(debug=True)
