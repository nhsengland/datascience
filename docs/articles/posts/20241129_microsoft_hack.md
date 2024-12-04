---
title: NHS x Microsoft AI Hackathon
authors: [AmaiaImazBlanco]
date: 2024-12-04
categories: 
    - NHS Websites
    - LLMs
    - Python
    - Events
links:
    - TBC
slug: microsoft-hackathon
description: >
    The NHS England Data Science team, as well as a range of other analysts from across the organisation, attended an AI Hackathon at Microsoft, organised by the Data Science Team together with Microsoft and Kainos, with the key stakeholders being the NHS Websites Team. 
---

> The NHS England Data Science team, as well as a range of other analysts from across the organisation, attended an AI Hackathon at Microsoft, organised by the Data Science Team together with Microsoft and Kainos, with the key stakeholders being the NHS Websites Team. In this article, the author shares her experiences at the event. 

<!-- more -->

Months ago, when I was invited to this hackathon, I sat at my desk and reluctantly signed up because everyone else was attending, sighing to myself about "please not another hackathon", and this was the energy I brought with me to the beautiful Storey Club, in Paddington, London, last week Tuesday. I thought "well at least I'll get a free lunch", but I was proven so wrong in my pessimism. Every team had either a Kainos or Microsoft representative, as well as a range of participants from across NHS England, including at least a few Data Science Team members per team. And unlike a usual hackathon, this one had stakeholders and well defined use cases, we were all working to one common goal. 

The use cases were outlined as: 

1. **Search & Summarise**: using an extract of the NHS Corpus developed by one of our PhD interns, Sam Hollands, (we used two websites worth of data, out of 600 NHS websites, and it was already 25GB worth of data!), we had to develop an LLM that used RAG to sift through that data and retrieve answers to queries based on these NHS websites.
2. **Explaining to a 12 year old**: Adapting the search and summarise for different personas, one of which being a 12 year old child
3. **Duplication & Conflict Detection**: comparing the two sites and identifying duplicate information and conflicting information.

The aim was for the websites team to have work to improve upon and be able to implement them in their websites. Having use cases meant that it was so much easier to split work up, and get our heads down, with no one in our teams finding themselves with nothing to do. It also meant we had a structured approach, making the experience so much more fulfilling. However, even with this, I was expecting that when it came to presenting, we'd end up watching 9 identical presentations, that just got slightly further along the process depending on the team. Once again, I was proved wrong by the creativity and range of approaches that the different teams took. We ranged from teams that had taken a thin slice approach to all three usecases, to teams that had gone really in depth in just one of them, to teams that had taken use case number 3 and made it into a tool that could be used by the websites team to improve the websites on the backend, removing conflict and duplication. 

Overall, I was left in awe by the creativity and technical skills of our team, as well as of all the other attendees. Hopefully the work gets used in the future by the websites team, and I hope that any hackathons I attend in the future are of this high quality! (Of course it did help that my team won)

![Picture of team 9, the winning team](../../images/microsoft-hackathon/team9.JPG)

The final results were: 

*First Place*: A thin slice approach of all three usecases, a project which included 4 of our very own data scientists: Sean Aller, Sudeshna Mallik, Xiyao Zhuang, and myself, as well as Rob Mansfield, Veta Ngammekchay, and our wonderful Kainos helper Peter Bodnar. 

*Second Place*: Contradiction Finder by Data Science's Ben Wallace, Matt Taylor, and Jenny Chim, as well as NHSE's Andrew Walker and Microsoft's Hannah Howell and Hanna Riaz. Focused on use case 3, making a usable tool for the websites team to find contraditions. 

*Third Place*: Data Scientists Chaeyoon Kim and Warren Davis, with Mary Amanuel, Piyali Dutta, and Farwah Kazmi from elsewhere in the NHS, together with Microsoft's Dan Watkinson and Josh Mercurio developed an AI career coach that was able to draw from and cite relevant information from the HEE website, and was easily customisable to improve communication towards different user personas.

![Team 9 presenting to a room full of people.](../../images/microsoft-hackathon/teampresentations.JPG)

Quotes from some of the attendees about their experience: 

**Bashir Abubakar**
> The hackathon was an incredible experience that not only allowed me to learn how to use Azure AI Foundry but also deepened my understanding of how large language models (LLMs) can transform healthcare, particularly within the NHS. My fascination with transformers began when I first read Attention is All You Need paper, which revolutionised the NLP space with its groundbreaking approach to self-attention. Seeing this theory in action, from research papers to practical applications, has been nothing short of inspiring.
The hackathon felt like a full-circle moment, as it opened new pathways for applying LLMs in healthcare, a vision I’ve long held for the future of AI professionals (Industry 4.0). It also reinforced the transformative role of prompt engineering, a skill I believe is pivotal in unlocking the potential of AI in creating meaningful solutions. 

**Will Poulett**:
> The variety of professions within each team was great, it's not often that GP's and data scientists can work together using generative AI. The solutions developed by each team were varied and interesting, I'm looking forward to seeing how they are implemented in the future!