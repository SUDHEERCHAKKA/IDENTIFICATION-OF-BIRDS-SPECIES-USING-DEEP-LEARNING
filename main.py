import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img,img_to_array

import numpy as np
from keras.models import load_model

model = load_model('C://Users//sudhir//Desktop//project birds//model.h5',compile=False)
lab = {0: 'ALEXANDRINE PARAKEET', 1: 'BALD EAGLE', 2: 'CROW', 3: 'DARJEELING WOODPECKER' ,4: 'EMPEROR PENGUIN', 5: 'GOLDEN PIPIT' ,6: 'HIMALAYAN MONAL', 7:'INDIAN PITTA', 8:'KIWI', 9: 'MYNA',10:'NICOBAR PIGEON',11:'OVENBIRD',12:'PINK ROBIN',13:'ROYAL FLYCATCHER',14:'STRIPPED SWALLOW',15:'TURKEY VULTURE',16:'YELLOW HEADED BLACKBIRD'}
def processed_img(img_path):

    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print(res)
    return res


def bird(result):
    if result == "ALEXANDRINE PARAKEET":
        st.write(
            "The Alexandrine parakeet (Psittacula eupatria), also known as the Alexandrine parrot, is a medium-sized parrot in the genus Psittacula of the family Psittaculidae. It is named after Alexander the Great, who transported numerous birds from Punjab to various European and Mediterranean countries and regions, where they were prized by the royalty, nobility and warlordsThe average weight of the Alexandrine parakeet bird is around 7.1 -10.6 oz (200-300 g).This species originated in India and Sri Lanka. The Alexandrine parakeet lives in forests, woodlands, agricultural lands, and mangrove forests of up to 3,000 feet in elevation.")
        st.subheader("check out this video  for more details : https://www.youtube.com/watch?v=Jkd4hgTfcvk")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//ALEXANDRINE PARAKEET//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//ALEXANDRINE PARAKEET//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Alexandrine Parakeet.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "CROW":
        st.write(
            "Crows are black birds known for their intelligence and adaptability, and for their loud, harsh.They also have a reputation for damaging crops; however, their impact may be less than previously thought. The genus Corvus comprises crows, ravens and rooks. These birds are all part of the Corvidae family, which includes jays, magpies and nutcrackers.There are about 40 species of crows. Crows can be found all over the world in a variety of habitats. For example, the American crow lives all over North America and prefers open areas — agricultural land and grasslands — with trees nearby. They also thrive in suburban neighborhoods, according to the ADW.")
        st.subheader("check out this video  for more details : https://www.youtube.com/watch?v=RG9kM9lLGLA")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//CROW//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//CROW//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//crow sound.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')



    elif result == "BALD EAGLE":
        st.write(
            "Bald eagles are iconic American birds and the only eagle species unique to and found throughout North America. Vagrant eagles appear on islands in Eastern Russia, Belize, Puerto Rico, and the U.S. Virgin Islands, usually after storms send them off course.The birds and their feathers were sacred to many Indigenous populations long before the bald eagle became the symbol of the newly formed United States in 1782. om their lazy food gathering habits to their surprising swims, discover more about the bald eagle.Up to 80% of eagles die of accidents or starvation before they reach adulthood, but those that do mature—at around 5 years old—typically live for 15 to 25 years.")
        st.subheader("check out this video  for more details : https://www.youtube.com/watch?v=qveV7SG9LrM")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//BALD EAGLE//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//BALD EAGLE//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Eagle Sound.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "DARJEELING WOODPECKER":
        st.write(
            "The Darjeeling woodpecker is a species of bird in the family Picidae. It is found in the northern regions of the Indian subcontinent, primarily in the Himalayas, and in some adjoining areas. Woodpeckers are tree-dwelling birds of the family Picidae, comprising subfamilies like Picumninae (piculets), Jynginae (wrynecks), and Picinae (sapsuckers). Their long, sharp bills that they use for pecking and drilling on trees help in distinguishing them from other bird species. They typically nest in the holes that they make in branches and tree trunks. Size: Woodpeckers vary in size, ranging from tiny piculets of length 7cm (2.8in) to the great slaty woodpecker measuring 48-58cm (19-23in). The possibly-extinct ivory-billed woodpecker and imperial woodpecker were larger than the great slaty woodpecker.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=XsF4HhVlHrE ")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//DARJEELING WOODPECKER//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//DARJEELING WOODPECKER//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Darjeeling Woodpecker.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "EMPEROR PENGUIN":
        st.write(
            "Emperor penguins are truly beautiful birds. Adults have a white stomach and a black head, back, tail and wings. They also have yellowy-gold markings on the side of their head and neck.Emperor penguins are the largest of all the different kinds of penguin. On average they measure 115cm tall – about the height of the average six year old. Emperor penguins spend their entire lives in Antarctica – the Earth’s southernmost continent – where temperatures can drop to as low as -60°C. Brrrr. These birds are super swimmers and impressive divers. They can reach depths of over 500m and stay underwater for up to 22 minutes! Sadly, today emperor penguins are considered near threatened and their populations are expected to decline rapidly in years to come.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=hrV5jiN7-yM")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//EMPEROR PENGUIN//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//EMPEROR PENGUIN//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Emperor Penguin.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "GOLDEN PIPIT":
        st.write(
            "The Golden Pipit (Tmetothylacus tenellus) is found in eastern Africa, where it inhabits grassland, savanna and shrubland.They are endemic to Ethiopia, Kenya, Somalia, Sudan, Tanzania and Uganda and occasional vagrants to Oman, South Africa and Zimbabwe. This species has an extremely large range, and hence does not approach the thresholds for Vulnerable under the range size criterion (extent of occurrence <20,000 km2 combined with a declining or fluctuating range size, habitat extent/quality, or population size and a small number of locations or severe fragmentation). The population trend appears to be stable, and hence the species does not approach the thresholds for Vulnerable under the population trend criterion (>30% decline over ten years or three generations).Found in dry savanna. Wanders widely, and most likely to be seen after rains. ")
        st.subheader("check out this video  for more details : https://www.youtube.com/watch?v=OB-_ohugcvY")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//GOLDEN PIPIT//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//GOLDEN PIPIT//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)

    elif result == "HIMALAYAN MONAL":
        st.write(
            "The Himalayan monal is a large colorful pheasant native to Himalayan forests. The adult male has multicolored plumage throughout, while the female, as in other pheasants, is more subdued in color. Notable features in the male include a long, metallic green crest, coppery feathers on the back and neck, and a prominent white rump that is most visible when the bird is in flight. The tail feathers of the male are uniformly rufous, becoming darker towards the tips, whereas the lower tail coverts of females are white, barred with black and red. The female has a prominent white patch on the throat and a white stripe on the tail. The first-year male and the juvenile resemble the female, but the first-year male is larger and the juvenile is less distinctly marked.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=qHUoX8TkDR0 ")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//HIMALAYAN MONAL//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//HIMALAYAN MONAL//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Himalayan Monal.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "INDIAN PITTA":
        st.write(
            "Indian Pitta in Gazipur, Bangladesh by Sifat Sharker The Indian pitta is a passerine bird native to the Indian subcontinent. It inhabits scrub jungle, deciduous and dense evergreen forest. It breeds in the forests of the Himalayas, hills of central and western India, and migrates to other parts of the peninsula in winter. Although very colourful, it is usually shy and hidden in the undergrowth where it picks insects on the forest floor. It has a distinctive two note whistling call which is heard at dawn and dusk. It is listed as Least Concern on the IUCN Red List as the population is considered large. The Indian pitta shows local migration. From October to March, these birds largely keep to the broad-leaved deciduous or semi-deciduous forested tracts of Southern India and Sri Lanka. Usually around mid-April, they begin their voyage north.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=49x21DohefU")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//INDIAN PITTA//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//INDIAN PITTA//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Indian Pitta.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "KIWI":
        st.write(
            "Kiwis are pear-shaped, flightless birds with long legs and beak. Though they look to be covered in fur, kiwis actually have thin, hair-like feathers. Their closest relatives are the emu, ostrich, cassowary and rhea. A kiwi is about the size of a chicken. There are five species. The largest is the northern brown kiwi, which grows up to 20 to 25 inches (50 to 65 centimeters) and weighs 3.2 to 11 lbs. (1.4 to 5 kilograms). The smallest is the little spotted kiwi. It grows up to 14 to 18 inches (35 to 45 cm) and weighs 4.3 lbs. (0.8 to 1.9 kg). Kiwis are typically nocturnal, which means they sleep during the day and are active during the night. Throughout the night, they spend their time foraging for food. Kiwis have a body temperature of 100 degrees Fahrenheit (38 degrees Celsius), the lowest of any bird, according to the San Diego Zoo.These birds get their names from the sound of their calls. They communicate with others by making kee-wee, kee-wee sounds.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=rb9aW2GYE24")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//KIWI//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//KIWI//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Kiwi Bird sound.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "MYNA":
        st.write(
            "The Common myna is a tropical bird with a strong territorial instinct, which has adapted extremely well to urban environments. This bird is readily identified by the brown body, black hooded head and the bare yellow patch behind the eye. Its bill and legs are bright yellow. There is a white patch on the outer primaries and the wing lining on the underside is white. The male and female look similar and are usually seen in pairs.Common mynas are native to Asia with their home range spanning from Iran, Pakistan, India, Nepal, Bhutan, Bangladesh and Sri Lanka; as well as Afghanistan, Uzbekistan, Tajikistan, Turkmenistan, Myanmar, to Malaysia, Singapore, peninsular Thailand, Indo-China, Japan (both mainland Japan and Ryukyu Islands) and China. These birds are typically found in a wide range of habitats with access to water; they inhabit open woodland, mangroves, grasslands, farmlands, orchards and urban areas.")
        st.header("check out this video  for more details :https://www.youtube.com/watch?v=nUAWqAq6T6k")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//MYNA//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//MYNA//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Myna Bird Sound.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "NICOBAR PIGEON":
        st.write(
            "The Nicobar pigeon is a large beautiful bird found mainly in South East Asia and Oceania. It is the only living member of the genus Caloenas and may be the closest living relative of the extinct flightless birds dodo and Rodrigues solitaire. Nicobar pigeons have developed a bright plumage; their head is grey, like the upper neck plumage, which turns into green and copper hackles. The tail is very short and pure white. The rest of their plumage is metallic green. The cere of the dark bill forms a small blackish knob; the strong legs and feet are dull red. Females are slightly smaller than males; they have a smaller bill knob, shorter hackles, and browner underparts. Immature birds have a black tail and lack almost all iridescence.Nicobar pigeons are found on small islands and in coastal regions from the Andaman and Nicobar Islands, India, east through the Malay Archipelago, to the Solomons and Palau. They inhabit rainforests, dry forests, mangroves, and shrubland.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=Rt4TCInxUtU")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//NICOBAR PIGEON//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//NICOBAR PIGEON//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Nicobar Pigeon.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "OVENBIRD":
        st.write(
            "Ovenbirds breed in large, mature broadleaf or mixed forests from the Mid-Atlantic states to northeastern British Columbia. They set up summer territories where the leaf canopy overhead inhibits underbrush and provides deep leaf litter hosting plenty of invertebrates. Extensive, uninterrupted forests with relatively closed canopies 50 to 70 feet above the ground seem ideal. Even fairly large forest patches of 250 to 2,000 acres may not be able to support Ovenbird populations unless larger forests are close by. Ovenbirds are less picky about their winter habitats. Ovenbirds eat mainly forest insects and other invertebrates: a range of adult beetles and larvae, ants, caterpillars, flies, and other insects. Most of these are hunted in leaf litter, some on leaves, and a few on bark or in the air. Parents feed ground beetles and larvae to nestlings.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=XSLHbBSFVjc")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//OVENBIRD//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//OVENBIRD//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Ovenbird.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')


    elif result == "PINK ROBIN":
        st.write(
            "The pink robin is a small passerine bird native to southeastern Australia. Its natural habitats are cool temperate forests of far southeastern Australia. Like many brightly coloured robins of the family Petroicidae, it is sexually dimorphic. Measuring 13.5 cm in length, the robin has a small, thin, black bill, and dark brown eyes and legs. The male has a distinctive white forehead spot and pink breast, with grey-black upperparts, wings and tail. The belly is white. The female has grey-brown plumage. The position of the pink robin and its Australian relatives on the passerine family tree is unclear; the Petroicidae are not closely related to either the European or American robins, but appear to be an early offshoot of the Passerida group of songbirds. ")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=iR-t04oPe5Q")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//PINK ROBIN//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//PINK ROBIN//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//BIRDSong_Robin.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')


    elif result == "ROYAL FLYCATCHER":
        st.write(
            "The royal flycatcher is a name used for roughly four species of birds in the genus Onychorhynchus within the family Tityridae. “Royal” refers to the exotic feather display on the crown of the bird’s head, which is a brilliant array of red, yellow, white, blue and/or black.The Royal Flycatchers use this brilliant, colorful plumage as a show of display during courtship rituals, after mating, while preening, in competition with other males over breeding or territory, or while being handled. Otherwise the plumed crest is lying flat.The royal flycatcher is a name used for roughly four species of birds in the genus Onychorhynchus within the family Tityridae. “Royal” refers to the exotic feather display on the crown of the bird’s head, which is a brilliant array of red, yellow, white, blue and/or black.The Royal Flycatchers use this brilliant, colorful plumage as a show of display during courtship rituals, after mating, while preening, in competition with other males over breeding or territory, or while being handled. Otherwise the plumed crest is lying flat.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=bSc1bi1u_f4")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//ROYAL FLYCATCHER//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//ROYAL FLYCATCHER//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Royal Flycatcher.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    elif result == "STRIPPED SWALLOW":
        st.write(
            "The lesser striped swallow is 15–10 cm long. It has dark blue upperparts with a red rump and a rufous-chestnut crown, nape and sides of the head. The underparts are white with dark streaking, and the upper wings and underwing flight feathers are blackish-brown. The underwing coverts are tawny. The blackish tail has very long outer feathers; these are slightly longer in the male than the female. Juveniles are duller and browner, with less contrast and shorter outer tail feathers. There are five or six subspecies differing in the extent of the underpart streaking.The lesser striped swallow has heavier and darker underparts striping, a deeper red rump, and a brighter head colour than the larger greater striped swallow.The lesser striped swallow builds a bowl-shaped mud nest with a tubular entrance on the underside of a suitable structure. The nest has a soft lining, and may be reused in later years. The nest may be built in a cave, under a rock overhang or a tree branch. This species has benefited from its willingness to use buildings, bridges, culverts and similar structures. Given the choice, it will select a high nest site.The eggs are glossy white sometimes with a few brown spots; three eggs are a typical clutch. Incubation is by the female alone for 14–16 days to hatching. Both parents then feed the chicks. Fledging takes another 17–19 days, but the young birds will return to the nest to roost for a few days after their first flight.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=qS8eNj6KZVk")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//STRIPPED SWALLOW//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//STRIPPED SWALLOW//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Striped-swallow.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')


    elif result == "TURKEY VULTURE":
        st.write(
            "The turkey vulture is in the same family (Cathartidae) as the California Condor (Federally endangered species) and the black vulture, which lives primarily in the south and southeast portions of the U.S.The turkey vultures scientific name is Cathartes aura which is Latin for cleansing breeze.Like all other vultures, the turkey vulture has a bald head. This is so that bits of carrion (dead meat) do not adhere to the skin as they would to feathers.The Turkey Vulture, with its bald red head and dark feathers, was given its common name due to its superficial resemblance to the Wild Turkey.At close range the naked red heads of the adult turkey vultures resemble those of turkeys, hence the name. Juveniles have pinkish black heads.Turkey vultures are the only scavenger birds that can't kill their prey. A close inspection of their feet reminds one of a chicken instead of a hawk or an eagle. Their feet are useless for ripping into prey, but the vultures have powerful beaks that can tear through even the toughest cow hide. They feed by thrusting their heads into the body cavities of rotting animals.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=Rh76p4NUCuM")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//TURKEY VULTURE//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//TURKEY VULTURE//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Turkey Vulture.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    else:
        st.write(
            "A golden head, black wings with a white patch, and a call sounding like the opening of a rusty farm gate, Yellow-headed blackbirds demand your attention. In spring, these birds are to be found in a marsh or slough where the surrounding water offers safety but often serves to limit the nesting habitat, resulting in crowding. A number of males are always in a display flight, head stooped, their feet and tail drooped, their wings beating slowly, in an accentuated manner. Some quarrel with their neighbors over boundaries; others fly off to feed. Approaching predators get mobbed by bunches of Yellow-headed blackbirds and any neighboring Red-winged blackbirds, nesting in the drier cattails. During summer, this species migrates north to go to the west-central areas of the United States and Canada. Its range extends to central-interior British Columbia in the far west, then directly south to the central-interior west coast and on to northeastern Baja California. In the east, the range runs from western Ontario to the north of Missouri. In winter, it is found from Texas to California and also in Mexico and as a casual visitor in Costa Rica. These birds inhabit freshwater marshes in the summer. They especially like to live amongst tule, cattails, and bulrush. At the time of migration and during winter they occur in open cultivated areas, in fields, and in pastures.")
        st.subheader("check out this video  for more details :https://www.youtube.com/watch?v=m1pEoenXySo")
        img1 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//YELLOW HEADED BLACKBIRD//001.jpg')
        img2 = Image.open('C://Users//sudhir//Desktop//project birds//shortlist//YELLOW HEADED BLACKBIRD//002.jpg')
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        st.image([img1, img2], use_column_width=False)
        audio_file = open('C://Users//sudhir//Desktop//project birds//sounds//Yellow-headed Blackbird.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')


def run():
    def set_bg_hack_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background: url("https://images7.alphacoders.com/402/402697.jpg ");
                 
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )

    set_bg_hack_url()
    st.title("𝙄𝙙𝙚𝙣𝙩𝙞𝙛𝙞𝙘𝙖𝙩𝙞𝙤𝙣 𝙊𝙛 𝘽𝙞𝙧𝙙𝙨 𝙎𝙥𝙚𝙘𝙞𝙚𝙨")
    page_bg_img="""
    <h4 style='text-align: left; color: #3DCAB5;'>* Data is based on "270 Bird Species"</h4>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)

    img_file = st.file_uploader("Choose an Image of Bird", type=["jpg", "png"])

    if img_file is not None:
        st.image(img_file,use_column_width=False)
        save_image_path = 'C://Users//sudhir//Desktop//project birds//uploads//'+img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        if st.button("Predict"):
            result = processed_img(save_image_path)
            st.success("Predicted Bird is: "+result)
            bird(result)
    st.subheader("Created By: Sai kumar, Sudheer")
run()

