---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} tags=["title"] -->
# Gaming the Qing Mandarinate: Digital Approaches to a Nineteenth-Century Chinese Board Game
<!-- #endregion -->

<!-- #region tags=["contributor"] -->
 ### Contributor1FirstName  Contributor1LastName [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/ORCID_ID) 
Institution 
<!-- #endregion -->

<!-- #region tags=["contributor"] -->
### Contributor2FirstName  Contributor2LastName [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/ORCID_ID_IF_EXIST) 
Institution
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["copyright"] -->
[![cc-by-nc-nd](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/) 
©<AUTHOR or ORGANIZATION / FUNDER>. Published by De Gruyter in cooperation with the University of Luxembourg Centre for Contemporary and Digital History. This is an Open Access article distributed under the terms of the [Creative Commons Attribution License CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/)

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["keywords"] -->
Qing dynasty (1644-1911), Bureaucracy, Boardgame, Graph Database, Monte Carlo
<!-- #endregion -->

<!-- #region tags=["abstract"] -->
How did prospective officials during the late Qing dynasty (1644-1911) learn about and perceive their career options? Our study explores the historical board game *Mandarin Promotions* (*Shengguantu* 陞官圖). As a career race played by dice, the game resembles Milton Bradley's famous nineteenth-century *Checkered Game of Life*. However, as it closely mirrors the actual Qing personnel system, *Mandarin Promotions* is much more complex. We studied a late nineteenth-century version reproduced with playable instructions by Puk Wing Kin in 2010, where players race from 22 starting positions through 434 positions distributed across 66 departments to reach 18 ranked final positions. Our goal was to answer three questions: How meritocratic was the imagined official career for the various starting positions which can be broadly categorized into hereditary privilege (including Manchu heritage), the imperial examinations, military merit and patronage, as well as what we call “incipient professionalism”? Secondly, which were the most pivotal positions for a career to the top echelons of the bureaucracy? Finally, given that office purchase is permitted by the game rules (as in the actual Qing bureaucracy) and that it is the only aspect of the game that gives players the opportunity to actively influence their fate, we ask under which circumstances purchasing office would be a good strategy.

Our exploration unfolds in two steps: First, we had to show that the game board indeed complied with the statutory promotion charts of the Qing bureaucracy. We did so by modeling the game and the promotion charts as networks of career paths (using Neo4J and Gephi) that lead through pivotal positions to the highest rank-classes. We found that the game board follows pre-1843 regulations, which confirmed its original creation in 1840, the year on the only surviving board that has a date. We argue that, while the real situation on the ground is not well explained by both the game or the Qing statutes, the game is a close enough mimicry of the statutory Qing bureaucracy to allow for generalizations about how contemporaries imagined their career options.

Secondly, we used a Monte Carlo simulation approach  to reveal the hidden biases of the Qing's monarchic system which defy common perceptions about a rational meritocratic bureaucracy. Hereditary privilege won big, examination enjoyed modest gains, all other paths lost. A second simulation including  purchase options showed that given the opportunity, players will overwhelmingly chose to engage in this possibility, confirming intuitions that office purchase ruins the suspense of the game. At the same time, uncertainty remains high even for purchasers, and rank purchase also does not eliminate the benefits of hereditary privilege. In conclusion, our playful engagement with the Qing mandarinate did yield new insights into how contemporaries navigated the world of career-making in a diverse yet monarchic society.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-1"] -->
## Introduction
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"u6jki": [{"id": "14298532/GE6RH8S7", "source": "zotero"}]}} -->
How did prospective officials during the late Qing dynasty (1644-1911) learn about and perceive their career options? Our study explores the historical board game Mandarin Promotions (Shengguantu 陞官圖), a career game where players start from multiple starting positions to race up the ladder of bureaucratic ranks. As a career race played by dice, the game resembles Milton Bradley's famous nineteenth-century Checkered Game of Life. However, as it closely mirrors the actual Qing personnel system, Mandarin Promotions is much more complex. Nonetheless, the game was highly popular among nineteenth-century Chinese people (<cite id="u6jki"><a href="#zotero%7C14298532%2FGE6RH8S7">(Culin, 1895)</a></cite>, 504-507). 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0utum": [{"id": "14298532/8EQW4XQE", "source": "zotero"}], "135yi": [{"id": "14298532/X6LTB4FQ", "source": "zotero"}], "cc03e": [{"id": "14298532/3TYGCHP7", "source": "zotero"}], "h2fca": [{"id": "14298532/VC6E2BGP", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Previous studies have focused on the history of Mandarin Promotions and similar promotion games in China which go back to the ninth century AD (<cite id="h2fca"><a href="#zotero%7C14298532%2FVC6E2BGP">(Morgan, 2004)</a></cite>, <cite id="cc03e"><a href="#zotero%7C14298532%2F3TYGCHP7">(Lo, 2004)</a></cite>, <cite id="0utum"><a href="#zotero%7C14298532%2F8EQW4XQE">(Sung, 2005)</a></cite>, <cite id="135yi"><a href="#zotero%7C14298532%2FX6LTB4FQ">(Ngai, 2010)</a></cite>). In 2010, the Hong Kong-based historian Puk Wing Kin published “Gaming the Mandarinate: Mandarin Promotions and China’s Official Culture.” He produced a playable version which included, for the first time, a detailed explanation of the rules. The author also copied an extensive explanation of the bureaucratic background from previous scholarship, thus making his book a textbook to introduce students to the Qing bureaucracy. Is this justified? Can we use a game to teach students about the Qing? 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
This paper explores this question through a comparison with Qing statutory regulations, using a network approach. After having confirmed the historicity of the game chart, we will ask, through a Monte Carlo simulation of the entire game for four players, how the nineteenth-century game designer(s) understood career chances for the different starting positions, as they mimic the emic notion of “*chushen* 出身,” the dividing line between commoner status and enfranchised holder of imperially sanctioned rank. Moreover, we will ask for the role of rank purchase which presents itself as a pervading feature of the game designer’s life world and also features prominently in the game.  

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"el0po": [{"id": "14298532/V9HJ834C", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Our analysis will be based on Puk’s explanation of the rules and the game board reproduced in his book. *Mandarin Promotions* game boards were ephemerals printed on paper, not wooden boards as we know from well-known board games like Chinese Chess or Go. The book includes two play charts: a xylographed board dated 1840 (held at the Oxford Bodleian library), and the reproduction of a lithography published in post-1870s Shanghai (<cite id="el0po"><a href="#zotero%7C14298532%2FV9HJ834C">(Puk, 2010)</a></cite>). The two charts are closely related. Both carry the same game rules and almost the same preface. On the later board, the date has been cut, some of the rules have been edited, and a few positions have been added, but the outline and most positions remain the same.  We will demonstrate that the 1840 chart was an original creation, while the later chart added few (if telling) changes.  Sections [1](#section-1) and [2](#section-2) of this paper will first explain the game, our data model, and our methodologies. This is followed by two specific studies exploring the realism and value judgement of the game setup as well as the nature of its multiple starting positions.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In section [3](#section-3), we will use a network approach to demonstrate that the 1840 designer of Mandarin Promotions, pursuing a didactic approach, followed statutory regulations of Qing bureaucratic careers so closely that later versions had to make some amends in order to make the overly complicated (if realistic) setup more playable. This does not mean that the game shows reality on the ground. Instead, we argue, based on new institutional studies, that the statutory regulations which have long informed our understanding on how the Qing empire worked did not perform much better than the game chart as a source of understanding historical reality. Both equally were “utopias of rule.” As the designers of the 1840 and the very similar 1870s versions of Mandarin Promotions also imbued the dice movements with value judgement by given numeric combinations meritocratic names like “virtue”, “talent”, or “effort”, studying the game’s moves and outcomes can also help us to understand how Qing contemporaries understood their own social reality.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"3036c": [{"id": "14298532/2XBUU6KC", "source": "zotero"}], "9iypg": [{"id": "14298532/EN5WKUSS", "source": "zotero"}], "gkegr": [{"id": "14298532/VXYXAJIC", "source": "zotero"}], "xh9ah": [{"id": "14298532/9YAWZZJ4", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In section [4](#section-4), we will use the case of the chushen provenances to show that the longstanding scholarly understanding of the Qing bureaucracy is not free from errors and omissions and could well take inspiration from the game. Chinese historiography has  long focused on the meritocracy of the civil service examinations. Although some scholars have noticed that there were alternative paths into officialdom, such as purchase or recommendation (<cite id="gkegr"><a href="#zotero%7C14298532%2FVXYXAJIC">(Ho, 1980)</a></cite>, 104; <cite id="9iypg"><a href="#zotero%7C14298532%2FEN5WKUSS">(Elman, 2000)</a></cite>, 126-127; <cite id="xh9ah"><a href="#zotero%7C14298532%2F9YAWZZJ4">(Zhang, 2023)</a></cite>), they have neglected the emic category of “*chushen*” as the dividing line between the commoner and the enfranchised holder of imperial status in the Qing status order. Even after the abolition of the civil service examinations in 1905, *chushen* was by no means abolished until the 1911 revolution (<cite id="3036c"><a href="#zotero%7C14298532%2F2XBUU6KC">(Chu, 2022)</a></cite>). In *Mandarin Promotions*, *chushen* provenances are modelled as the starting positions that the players first enters the game on. But do these positions grant an equal playing field? Or do some chushen have better opportunities than others to get ahead and win money in the game? Finally, what effect does the purchase of office have on the outcomes of the game? Does it level the playing field? We explore these questions  using a Monte Carlo simulation which, given the complicated structure of the game, required an implementation of the game rules in a program with considerable complexity. The outcomes show that *Mandarin Promotions* as a dice game maintains suspense by giving most *chushen* positions equal chances to move up the ladder of official ranks under great uncertainty. However, the actual monetary winning chances show the inequities of the system of promotions, giving advantages to hereditary privilege and Imperial grace. Purchase, the only instance where the player can exert strategy, slightly levels the playing field, but does not eradicate privilege. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Why should we bother to study a historical board game anyway?
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"j3aa5": [{"id": "14298532/SDB4J2CY", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In 1887, on a night of the Chinese New Year’s celebrations, a group of literati in Shanghai played a few rounds of the board game *Mandarin Promotions*. One of them put his thoughts into a poem published the next day in the *Shanghai Daily* (*Shenbao*, <cite id="j3aa5"><a href="#zotero%7C14298532%2FSDB4J2CY">(桂笙 Guisheng, 1887)</a></cite>, HistText database):

>Take easy a dice bowl, set a square buffet.
> 
>Imperial offices spread out, all play.
>
>Merit and fame, on paper, come like a dream.
>
>Good offices in fact are all up for pay.

There is a double denial of realism in this poem. In line three, there is the dice game vs. the reality of official careers, one being easy and equitable, the other one hard to attain. Line 4, by contrast, evokes the official career as it ought to be, vs. the reality of widespread venality where official rank could simply be purchased, and even legally so. 
<!-- #endregion -->

This paper suffers from a similar dissonance. Are we talking about the game or about bureaucratic reality? One could argue, as one reviewer did, that “using this [the game] to discuss real world situation[s] is akin to using Monopoly to talk about the conditions of the turn of the century American housing market. It is not convincing.” If we followed his advice, this would be a study about a board game, nothing else. However, we still argue that the game makes a meaningful comment on a bureaucratic reality. Even more, the game is so dense in context that it would not have been playable without an understanding of that reality. Equally, we would be totally unable to write anything about this game without frequent reference to the bureaucratic institutions of the Qing. Therefore, we will go ahead referring to both the game and Qing bureaucracy. And, to start with a disclaimer, even the best efforts to tell the two apart will not be able to forestall all misunderstandings on the part of the unfamiliar reader.


<!-- #region citation-manager={"citations": {"fzjit": [{"id": "14298532/3TYGCHP7", "source": "zotero"}], "ljx3w": [{"id": "14298532/XRLLY3EK", "source": "zotero"}], "x7amp": [{"id": "14298532/DEYG8UIS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In fact, we are not the first who conflate Mandarin Promotions with reality. As early as in 1687, a Jesuit convert introduced the English librarian Thomas Hyde to the game, although in an earlier civil-military version played with six dice. Hyde not only used it to introduce the Chinese bureaucracy to his audience; it also served him as proof that the Enlightenment idea of China’s bureaucratic rule by merit was a myth after all. In 1877, Hyde’s Bodleian Library obtained another chart, this time for civil offices only, which is precisely dated 1840 and already close to the version used in our paper. The cataloger, none less than the eminent Sinologist James Legge, mistook it for “an official directory” (“Qing Guan Ce 清官冊, see <cite id="ljx3w"><a href="#zotero%7C14298532%2FXRLLY3EK">(Helliwel, 2014)</a></cite>). Or, perhaps Legge knew that it was a game and only failed to make a note, when he jotted down an alternative name common for Mandarin Promotions in China, leading to misunderstandings among later librarians. But then, couldn’t it have been the intention of the creators to set the game in a realistic context?  Another one hundred years later, the anthropologist Leon Stover described the game in great detail to make a grand sociological argument about nothing less than The Cultural Ecology of Chinese Civilization. Stover indeed compared Mandarin Promotions to Monopoly. Instead of real estate and wealth, players compete for political power, because, as Stover put it, “in the Chinese Agrarian State. Power is the origin of wealth” (<cite id="x7amp"><a href="#zotero%7C14298532%2FDEYG8UIS">(Stover, 1974)</a></cite>, 215; <cite id="fzjit"><a href="#zotero%7C14298532%2F3TYGCHP7">(Lo, 2004)</a></cite>, 66). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"aq1ns": [{"id": "14298532/DJQAH7XE", "source": "zotero"}], "c0s55": [{"id": "14298532/MGTNKIZA", "source": "zotero"}], "dz7so": [{"id": "14298532/X6LTB4FQ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
The list of game-reality conflation does not end here: May-ying Ngai cites the anecdote that Pao Chao Hsieh (Xie Baoqiao 謝保樵, 1896-1960), author of an influential English-language introduction to the bureaucratic system of the late Qing dynasty in 1925, used *Mandarin Promotions* to entertain fellow students and professors and was rumored to have based the book “on his favourite plaything” (Ngai, May-Ying Mary. <cite id="dz7so"><a href="#zotero%7C14298532%2FX6LTB4FQ">(Ngai, 2010)</a></cite>, p. 3, fn. 3). The book is: <cite id="aq1ns"><a href="#zotero%7C14298532%2FDJQAH7XE">(Pao Chao Hsieh, 1925)</a></cite>. It originated from his Ph.D. dissertation. Endymion Wilkinson places a note on Mandarin Promotions in chapter 3.17 “Central & Local Government” not in chapter 24.14. “Sports & Games” (<cite id="c0s55"><a href="#zotero%7C14298532%2FMGTNKIZA">(Wilkinson, 2012)</a></cite>).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"856xm": [{"id": "14298532/WJGDPPDF", "source": "zotero"}], "e04q2": [{"id": "14298532/S5JC8IGD", "source": "zotero"}], "go665": [{"id": "14298532/YEVRUWRU", "source": "zotero"}], "zwihl": [{"id": "14298532/AJMN2YBW", "source": "zotero"}]}} editable=true raw_mimetype="" slideshow={"slide_type": ""} -->
Actually, we believe that the Indian *Game of Knowledge* or Tibetan *Game of Liberation* (in more or less decontextualized versions known in the US as Milton Bradley’s *Checkered Game of Life or Snakes and Ladders*) would make for a better comparison (<cite id="go665"><a href="#zotero%7C14298532%2FYEVRUWRU">(Schmidt-Madsen, 2019)</a></cite>; <cite id="856xm"><a href="#zotero%7C14298532%2FWJGDPPDF">(Tatz &#38; Kent, 1977)</a></cite>). However, even *Monopoly*’s alleged divergence from reality was not as straightforward as it might appear. Decades before Charles Darrow plagiarized the game and Parker Brothers turned it into a celebration of capitalism, the game was patented by Elizabeth Magie, a follower of Henry George, as the *Landlord’s Game* to uncover the evils of a (real) monopolist housing market (<cite id="e04q2"><a href="#zotero%7C14298532%2FS5JC8IGD">(Pilon, 2015)</a></cite>). In the early 1980s, in still Communist East Germany Martin Böttgers invented a game “Bürokratopoly” to reflect in an ironic way on his society. Unconsciously mirroring Stover’s description of Qing China, Böttger later motivated his shift away from *Monopoly*’s money nexus by the political realities of a communist state: „In a centralized bureaucracy of functionaries, like the GDR, it was the pursuit of social advancement, of power, that held the system together” (<cite id="zwihl"><a href="#zotero%7C14298532%2FAJMN2YBW">(DDR-Museum, n.d.)</a></cite>). In a quirky detour across a game board, sociological analysis and political comment found similarities between Qing China and Communist East Germany: Power had won over wealth.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"hixpm": [{"id": "14298532/3TYGCHP7", "source": "zotero"}], "hvpo9": [{"id": "14298532/I2NEPQBN", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In short, games are abstractions of, but also comments (and value judgements) on the real world, and they have frequently been understood and used as the latter. Needless to say, the degree of abstraction and the closeness of comments stand in an inversely proportional relation with each other. Go (*Weiqi* 圍棋) signifies the battle between white and black forces. It is low in historical context and, hence, a world game. By contrast, no one plays *Mandarin Promotions* today, except for Chinese history nerds. We argue here that *Mandarin Promotions* is context-dense. It is as low in the level of abstraction as one could get without losing the (game) plot. It is, accordingly, high in comment (we will cite evidence in section 3). This is also the reason why context-dense games are frequently used as historical or social teaching tools. The *Landlord’s Game* was created with didactic intent. So was *Mandarin Promotions*. It was exempted from gambling bans and played in a ritualized context (during New Year). Similar games have a long history in China. The oldest version named *Han Officials*, whose rules have been preserved in writing, was created in the eleventh century AD to teach the bureaucratic system of the first century BC. Not only did educators use it as a teaching device for the study of the Western Han dynasty. The game was also cited as historical evidence by later historians. The game hence created historical knowledge for generations of scholars (<cite id="hvpo9"><a href="#zotero%7C14298532%2FI2NEPQBN">(L. Zhang, 2023)</a></cite>. The game is Liu Ban’s 劉攽 (1022-1088) “Han Guan Yi 漢官儀”. For more on the history of promotion games: (<cite id="hixpm"><a href="#zotero%7C14298532%2F3TYGCHP7">(Lo, 2004)</a></cite>)). *Bürokratopoly* is now marketed to schools by the DDR Museum to make students in the FRG (1949-today) understand life in the GDR (1949-1990), which also no longer exists, much like the game Han Officials recreated Han China (202BC-220AD) for Song (690-1276) people and Mandarin Promotions recreates Qing China (1644-1911) for people living in today’s Sinophone communities.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"00e12": [{"id": "14298532/387PSRU9", "source": "zotero"}], "de7as": [{"id": "14298532/Q5VDL4VL", "source": "zotero"}], "fffmu": [{"id": "14298532/G53Z38BI", "source": "zotero"}], "i8fvu": [{"id": "14298532/387PSRU9", "source": "zotero"}], "x27c5": [{"id": "14298532/DVDEVB62", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Why should we bother to study this game then? Since Johan Huizinga has famously made play into a field of serious academic study (<cite id="x27c5"><a href="#zotero%7C14298532%2FDVDEVB62">(Huizinga, 1950)</a></cite>), scholars have long crossed the invisible line between game and society. Roger Caillois subsumed play and games under four categories—agon (competition), alea (chance), mimicry (simulation), and ilinx (vertigo)—and applied these categories freely to society. Since modern societies suppress the latter two, he argues, modern political systems are left with a precarious equilibrium between agon (merit, competition) and alea (chance, inheritance, lot) (<cite id="fffmu"><a href="#zotero%7C14298532%2FG53Z38BI">(Caillois, 2001)</a></cite>, 109-110). The applicability of this idea to a competitive career game appears obvious. But the remarkable fact that *Mandarin Promotions* almost entirely relies on alea should give a pause to those who still believe that Chinese officials were recruited by meritocratic competition. Bourdieu has made copious use of the game metaphor to explain how people operate within social fields by getting “a feel for the game,” although he believed that they are more successful if they are quasi born into it, making the social game an unequal one (<cite id="de7as"><a href="#zotero%7C14298532%2FQ5VDL4VL">(Bourdieu, 1990)</a></cite>, 66-68 and passim).  David Graeber, by contrast, considered the game an “utopia of rules,” a sheltered space where rules exist and are known to all participants, so that an equal playing field becomes possible (<cite id="00e12"><a href="#zotero%7C14298532%2F387PSRU9">(Graeber, 2015)</a></cite>, 198-191). Graeber has described the intrusion of rules even into anti-bureaucratic phantasies like Dungeons & Dragons as a process of bureaucratization, calling rule-based games a “bureaucratic fantasy.” At the same time, bureaucracies themselves also create games, i.e. rule-based playing fields, “they’re just games that are in no sense fun” (<cite id="i8fvu"><a href="#zotero%7C14298532%2F387PSRU9">(Graeber, 2015)</a></cite>, 190). In *Mandarin Promotions*, as we will show, the two come together, but they still are fun.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"6qijk": [{"id": "14298532/9PCJFR3C", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We think that it is not too far-fetched to see *Mandarin Promotions* as a form of mimicry, as it simulates the career-making process quite faithfully from the Imperial examinations to the triennial performance reviews. At the same time, we argue that *Mandarin Promotions* was a mimicry, not of the real bureaucracy in Qing China, but of the statutory bureaucracy. The statutory bureaucratic system, outlined in imperial statutes and regulations, has long been used as the guideline of how the Qing bureaucracy functioned (<cite id="6qijk"><a href="#zotero%7C14298532%2F9PCJFR3C">(Metzger, 1983)</a></cite>). By the time our game was created and revised, after 1840, however, it had long become an “utopia of rules” which was almost as far from reality on the ground as the game board itself. The double dissonance of our poet in the beginning of this section mirrors this fact. After explaining the basic set-up of the game and our approach to modelling it in the next section, we will show in section [3](#section-3) how the game recreated the statutory system and how it imbued it with value. Section [4](#section-4) will then look at the entry, i.e. the different starting positions, to show that the game, mirroring real life, was not entirely an equal playing field.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-2"] -->
## Housekeeping: How did we model the data?
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Game Rules
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
*Mandarin Promotions* is a board game played with dice — in our version four, but up to six in other versions — by an unspecified number of players. The rules are printed on the game chart, and players who understand Chinese have no trouble following these rules if they are willing to learn the 434 positions in 66 departments and their significance for career making in the Qing bureaucracy (Arguably, players could simply learn these positions by rote, but without any interest in their bureaucratic meaning such an exercise would hardly make sense.). The departments represent institutions of the Qing bureaucracy, including both brick-and-mortar administrative offices (*yamen* 衙門) like ministries and normative institutions from the organization of local, provincial, and metropolitan examinations to groups of courtly titles and rewards. The positions represent actual steps on the bureaucratic career ladder. The goal is to race from 15 starting positions (*chushen* 出身) to reach the highest-possible rank, or at least a higher rank than the other players. At the same time, the game is also played for money. There are two types of wager: pool-money (every player puts in 100 chips at the beginning of the game) and player-money. Specific positions contain instructions to pay money from pool to player (rewards), from player to pool (fines, purchase of office), or from player to player (gifts). This means that even though there is a fixed pool of money in the beginning, more money can be lost or won than the total of the initial pool (more on this in section (4)[section-4]). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"gehra": [{"id": "14298532/V9HJ834C", "source": "zotero"}]}} -->
To fully explain the game rules would exceed the scope of this paper. We refer the reader to Puk Wing Kin’s study (<cite id="gehra"><a href="#zotero%7C14298532%2FV9HJ834C">(Puk, 2010)</a></cite>). Here, we will introduce the game board, as well as the main positions and moves. We cannot spare the reader of some explanation of the bureaucratic concepts which underpin them.

<!-- #endregion -->

### The Game Board

<!-- #region editable=true slideshow={"slide_type": ""} -->
*Mandarin Promotions* is a career game which belongs to the family of life games derived from the Indian *Game of Knowledge* (not unlike the *Checkered Game of Life* or *Snakes and Ladders*). However, *Mandarin Promotions* is neither a game of salvation nor a mere race game (like the *Game of the Goose*). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"i01co": [{"id": "14298532/YCJWD8HN", "source": "zotero"}]}} -->
Firstly, the game is an imperial metaphor. In life games, the goal is at the end or on top of the chart (salvation, retirement), whereas in *Mandarin Promotions* the goal is in the center. In the earlier or simplified versions, the center depicts the gate of the forbidden city, symbolizing the emperor. In our nineteenth-century game chart, the square in the center contains the rules of the game. It is also the place into which a bowl is placed to throw the dice. The throne is conceived as the center of arbitrary power, while the bureaucracy is arranged in concentric circles around it, starting from courtly titles and offices, to the metropolitan bureaucracy, to the provincial administration, the civil service examination, and the system of promotions and penalties on the outermost circle. We have an almost perfect depiction of the dynastic realm (<cite id="i01co"><a href="#zotero%7C14298532%2FYCJWD8HN">(Duindam, 2015)</a></cite>, 5).

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Secondly, the world imagined by *Mandarin Promotions* is not an equal playing field. In life games, there is only one starting position, and it is usually the first square or field *within* the game, often designated “birth” or “go” (as in *Monopoly*). There is also only one final position. In *Mandarin Promotions*, players start from outside the game (The term “*juwai* 局外”, lit. “outside the game”, today also denotes the “outsider,” *juwairen* 局外人, in general.
). The first roll of the dice determines from which of the fifteen starting positions the player will start. In addition, there are a number of hereditary titles of nobility attained with “lucky” (all equal, i.e. having a chance of only (⅙)<sup>4</sup> < 0.08% occurring) dice only. The starting positions correspond to the real-life notion of “*chushen* 出身”, lit. provenance. These are qualifications which lock the holder into certain career paths (more on them below and in section [4](#section-4)). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"ws1xc": [{"id": "14298532/SQFMMJP7", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Thirdly, fate is the driving force of career development. Similar to life games, Mandarin Promotions is played by dice with little room for strategy or choice. The next step following certain dice rolls is always spelled out in words below each position. Even China’s famed meritocracy (<cite id="ws1xc"><a href="#zotero%7C14298532%2FSQFMMJP7">(Elman, 2013)</a></cite>) is represented as fateful. Dice combinations are not counted numerically but numinously. They are imbued with value: <span style="font-variant: small-caps;">virtue</span> (Double-4), <span style="font-variant: small-caps;">talent</span> (Double-6), <span style="font-variant: small-caps;">effort</span> (Double-5), <span style="font-variant: small-caps;">mediocre</span> (Double-3), <span style="font-variant: small-caps;">weak</span> (Double-2), <span style="font-variant: small-caps;">corrupt</span> (Double-1, can be cancelled by a 4). One could argue that the dice combinations signify merit in a countable way, contradicting the above contestation that the vision of the game is less rational-meritocratic than expected. However, merit is defined by fortune (dice) alone (This is also the case in the Tibetan *Game of Liberation*.). There are also “lucky” dice without numinous names, particularly four equals (*quanse* 全色) and 3-4-5-6 (*chuanhua* 穿花, garland), and they always ensure the best career moves. Only one provision in the rules  allows some agency to the player: the purchase of an office.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["subsection-2.3"] -->
### The Positions
<!-- #endregion -->

Starting from the *chushen* positions, players move their game piece from position to position with each further roll of dice according to the instructions printed on the board. From each position five to six other positions can be reached, based on the dice values specified above. While there are six combinations of dice, some positions specify that when rolling one of the two worst cases, <span style="font-variant: small-caps;">corrupt</span> or <span style="font-variant: small-caps;">weak</span>, the player simply remains at their current position.
 For an unfamiliar viewer, all positions with their follow-up instructions look similar, but they are not. 


<!-- #region editable=true slideshow={"slide_type": ""} -->
Firstly, there are the fifteen *chushen* starting positions in department C1 for which special dice values other than the sequence from <span style="font-variant: small-caps;">virtue</span> to <span style="font-variant: small-caps;">corrupt</span> described above apply.  In addition, titles of hereditary nobility (C2) are also reached with the first roll of dice, namely with four equals. Table [5](#table-41-*) in section [4](#section-4) lists the *chushen* positions and titles of nobility as they appear on the game chart. These starting positions correspond to a real-life concept which is a neglected category in the Western historiography of China where it is generally misunderstood as one of three degrees in the civil service examinations. However, out of fifteen *chushen* positions on our game chart, only three are related to the famous civil service examinations. This is different from the seventeenth-century boards where the examinations were the dominant path into office. We hypothesize that *chushen* not only come in different facets, but also determine the career chances of their holders. How *chushen* provenances are related to quantifiable career chances will be the topic of section [4](#section-4) of this paper. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Secondly, the goal of the game is to rise in rank-class and move to retirement at the highest possible rank-class. The player ends the game by moving his game piece into the final section titled “Examination of Rank-Classes” (*pinjikao* 品級考) either from their last main position (rewarded retirement, *he* 賀 or *dahe* 大賀) or from a performance or penalty position (honorable retirement, *yugao* 予告, or dishonorable retirement, *xiuzhi* 休致), more on the latter in a moment. The names of these final positions do not matter here. There are 18 rank-classes, with 1a being the highest and 9b the lowest (the very lowest unclassed category is not listed in the final section). The final rank class attained in retirement is equal to the rank of the position previously held.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Thirdly, out of 434 positions, only 338 are reachable with the primary game piece. These regular positions include the *chushen* positions (C1) and titles of hereditary nobility (C2) which are reached by the first dice roll. The remaining positions correspond to steps in the civil service examinations or to ranked offices in the bureaucracy.  Knowledge of the location of these 272 ranked offices–in the provinces (82), in Beijing (190)–is indicated by their position on the game board. Location is important in the real Qing bureaucracy and vital to analyse the game, as we will see in section [3](#section-3). Ranked positions reflect vacancies in the bureaucratic system rather than numbers of officials. For example there are two positions for county magistrate in busy and simple counties (P93, P94, *zhixian* 知縣, 7a) on the game board and one position for Minister of Revenue (P223, *hubu shangshu* 戶部尚書, 1b), while in reality there would be about 1300 magistrates, but only two ministers. Hence, the capital is overrepresented in terms of positions.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Fourthly, another 96 positions are reserved for a secondary game piece which is placed on them while the primary piece remains in its position. In the next round, after throwing the dice, the instruction that is prescribed by the secondary position for the combination of dice is applied to the primary game piece, or in some cases, again to the secondary piece. In case the instruction specifies an action for the primary piece, the secondary piece is then withdrawn. These temporary positions mimic three institutions in the Qing bureaucracy:
1.  Performance reviews taking place every three years, most prominently the triennial reviews for provincial officials (C12, *daji* 大計, Great Reckoning) and for officials in the capital (C10, *jingcha* 京察, Capital Evaluation). There also is a military merit section (C9, *jungong* 軍功) and a penalty section (C13, *chufen* 處分). A dice roll of corrupt (D-1) can lead into the penalty section, both from a main position and from one of the performance review sections. (25 positions altogether)
2.  Commissions (*chaishi* 差使), i.e. temporary work assignments while the main position or rank is on hold. They are distributed across departments. (38 altogether)
3. Special honorary rewards and titles meted out by the emperor. Honorifics are special awards (C64, *te’en* 特恩) like the peacock-feather plume decorations (P413 *hualing* 花翎) or titles of nobility (C63) like marquis (*houjue* 侯爵). Palace titles (*gongxian* 宮銜, C60) like “senior protector of the heir apparent” (*taizi taibao* 太子太保) are a special case because they are between ranked positions and honorifics. (33 altogether).


<!-- #endregion -->

Fifthly, the positions that have been visited by a player during the game can have a definite impact on the player later on , because a small number of movements is restricted to those who have previously attained a particular status. In real life, such a status could have been inherited (i.e. being a Manchu or having inherited a title of nobility) or obtained (i.e. by passing the imperial examinations). In the game, status is obtained by being sent per dice to visit a certain position. For example,  access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士, rank-class 1b) is limited to those that have “become” Manchu by having visited a Manchu position before. This mechanism both adds another layer of realism to the game, and makes the digital exploration significantly more difficult, because it makes it impossible to treat it as memoryless, i.e. in a fashion where the current state of the game board is all that matters.


<!-- #region citation-manager={"citations": {"vmewr": [{"id": "14298532/T54NP4X3", "source": "zotero"}], "y2epw": [{"id": "14298532/CTD5EWCD", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Finally, a word on translations. Our charts and tables will add translations to the Chinese names and titles. All translations are taken from Charles Hucker’s *Dictionary of Official Titles*. This work is not the best reference for the late Qing. However, it is well established within the Digital Humanities community, because it cuts across dynasties and because of US-American dominance in the field (<cite id="y2epw"><a href="#zotero%7C14298532%2FCTD5EWCD">(Hucker, 1985)</a></cite>. Hucker often translates terms that are identical in Chinese with different terms in English, taking into account different functions and status of similar sounding offices. For our purposes, this method creates rather disturbing inconsistencies. Brunnert und Hagelstrom, written originally by Russian diplomat-researchers in 1910, provides a better guidance for the late Qing officialdom (<cite id="vmewr"><a href="#zotero%7C14298532%2FT54NP4X3">(Brunnert &#38; Hagelstrom, 1912)</a></cite>)). Since for Chinese-speaking readers, these translations are unrecognizable gibberish, the original names will be maintained. Where we cannot include both into one figure, we will provide two versions of the charts.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Career paths as network

<!-- #endregion -->

Based on its characteristics, it is possible to re-imagine *Mandarin Promotions* as a network, in which the positions are the nodes and the dice rolls are the edges. *Chushen* starting positions only have one incoming edge (from outside the game). Final positions have no outgoing edges. All other positions can only have up to six outgoing edges, but should be expected to have at least one incoming edge (in reality, they often have many more). However, there are in fact positions in the game such as P29 and P30, both types of meritorious “tribute” students at the Imperial Academy, that have no incoming edges, that is, the game designer did not include any rule to move to these positions, so that nobody can ever get there. Our hypothesis is that the game designer aimed for completeness in his representation of available positions in the real bureaucracy, but could not come up with a dice move, because he was constrained by the limit of six outgoing edges per position.


<!-- #region editable=true slideshow={"slide_type": ""} -->
The network structure obtained in this way is not a social network, of course, but rather resembles a transport network where the career paths are routes through the nodes, and nodes with many incoming paths are important positions that, over several playthroughs of the game, many players will pass through in their careers. Strictly speaking, these career paths only lead through 338 nodes, while the 96 temporary positions for the secondary game piece are modelled as additional  states of the main nodes. However, the latter can also be understood as a furlough between position — go to position x and wait until a decision for your next move. When Author A first conceived of the game in network terms, the treatment of these temporary positions posed considerable trouble. When she implemented the network in Neo4J, she made the decision to distinguish between the two types of nodes by imposing a uniqueness constraint on the 338 regular nodes (hence dubbed “uniquenodes”) while new temporary nodes were created each time for the temporary positions (hence dubbed “concurrentnodes”). This pushed up the total number of nodes to over 4,000 which complicated the resulting network graph, resulting in  a hairball effect, i.e. an overly dense structure, but it created a precise representation of the game moves.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
A condensed version of the resulting graph is shown in [1](#figure-32-*), grouping positions into clusters based on their type (e.g. starting positions “Start”, positions having a rank “Ranked” and so on).  Edges represent dice rolls. MERIT stands for doubles. LUCK stands for four equals, 3456, 1133 etc., i.e. dice rolls with lower probability):

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
>call db.schema.visualization()
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-32-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Data Model"
            ]
        }
    }
}
display(Image("media/DBSchema.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Since Neo4J proved too unwieldy to be handled for further analysis, Author A exported the data to Gephi.  This method yielded valuable results for historical comparison which will be discussed in section [3](#section-3). However, the simple network approach had limits. First, Gephi is built to study social networks and thus does not perfectly fit the game, which only uses directed edges and can be most fruitfully studied with methodology for transport networks. Secondly, a network  graph also could not accurately answer our question if all of the fifteen starting positions have the same opportunities in the game. As explained above, the game mimics reality by forcing the player to keep track of status inherited or obtained previously. Some positions higher up in the hierarchy represented in the game are hence limited to people having visited a particular position earlier in the game.  Using a network as the model, it is difficult to study such rules relying on memory. Thirdly, calculating monetary gain or loss also proved difficult.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Here is where a programmatic approach proved superior. Based on the existing data in the Excel worksheet and a new reading of the rules, Author B has implemented a Monte Carlo simulation of the game in Python with a large number of playthroughs to determine competitive chances and monetary gains. The results of this exploration will be discussed in section [4](#section-4).

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-3"] -->
## “Utopias of Rules”? The Real and the Gamified Qing Bureaucracy
<!-- #endregion -->

### Hidden Rules

<!-- #region citation-manager={"citations": {"3lskv": [{"id": "14298532/XZSI5NY6", "source": "zotero"}], "fxpny": [{"id": "14298532/T4BB86FW", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
If we argue that *Mandarin Promotions* is both mimicry of and a comment on reality, we have two types or sources to find out specifics. One is statements of game designers or players. The other is the game design itself. For comparison, we also need to consider the sources of this game design which lead us to better understand the relation to the (statutory) bureaucracy. The idea of “hidden” meaning has been inspired by an obsession with “hidden rules” in Chinese political discourse since the 2000s which went back to Wu Si’s eponymous bestseller (<cite id="3lskv"><a href="#zotero%7C14298532%2FXZSI5NY6">(Wu, 2009)</a></cite>). It reflects the belief that China’s beautifully well-ordered and meritocratic political system, a view shared by prominent Western observers (<cite id="fxpny"><a href="#zotero%7C14298532%2FT4BB86FW">(Bell, 2015)</a></cite>), actually works very differently from its public regulatory face. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"39ik4": [{"id": "14298532/V9HJ834C", "source": "zotero"}], "k3ozb": [{"id": "14298532/X6LTB4FQ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We have cited player opinion in the poem at the beginning of section [1](#section-1). The game board itself contains a preface of the anonymous game designer which states the following: “Based on the *Collected Statutes* (*Huidian* 會典), we have made a comprehensive table of official ranks, complete for Manchu and Han officials, and differentiated between the regular and irregular paths. It is not just a game, but faithfully lets the distinctions of official ranks and the understanding of their qualifications be clearly spread out in one table, in order to be of great service” (<cite id="39ik4"><a href="#zotero%7C14298532%2FV9HJ834C">(Puk, 2010)</a></cite>, 22; for a full, but slightly different translation see: <cite id="k3ozb"><a href="#zotero%7C14298532%2FX6LTB4FQ">(Ngai, 2010)</a></cite>, 76). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"2197m": [{"id": "14298532/MGTNKIZA", "source": "zotero"}], "54tvu": [{"id": "14298532/9GEGGN5R", "source": "zotero"}], "piarh": [{"id": "14298532/9YAWZZJ4", "source": "zotero"}], "x23c9": [{"id": "14298532/EN5WKUSS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The designer, first, declares that his Mandarin Promotions is an accurate reference work reflecting his contemporary bureaucratic system. He, secondly, manifests faithfulness by citing the major compendium of Qing administrative law (<cite id="54tvu"><a href="#zotero%7C14298532%2F9GEGGN5R">(Keliher, 2016)</a></cite>. For the translation of the term “huidian” see: <cite id="2197m"><a href="#zotero%7C14298532%2FMGTNKIZA">(Wilkinson, 2012)</a></cite>, 843. This reference work (pp. 253-268) also contains the best concise introduction into the structure of the Qing bureaucracy.). Thirdly, he claims comprehensiveness by including the major status distinctions between Manchus and Han, as well as different “paths” into officialdom. What he refers to as “regular path” mainly refers to the imperial examinations. The “irregular path” mainly refers to office purchase, referred to by the poet in section [1](#section-1), which was perfectly legal albeit “irregular” (<cite id="x23c9"><a href="#zotero%7C14298532%2FEN5WKUSS">(Elman, 2000)</a></cite>; <cite id="piarh"><a href="#zotero%7C14298532%2F9YAWZZJ4">(L. Zhang, 2023)</a></cite>).

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"betaf": [{"id": "14298532/MNBH9DQS", "source": "zotero"}], "pybej": [{"id": "14298532/9XED7GPL", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The *Collected Statutes* mostly contain regulations and imperial decisions on specific cases (“*shili* 事例” which were collected as “*Huidian shili* 會典事例”). To make these into a game would have been a daunting task. Fortunately, the *Collected Statutes* also contain chapters titled “Examination of Rank-Classes.” Their Chinese name is “*Pinji Kao* 品級考”, and this is also the name of the department on the game chart which marks the final goal of the game. Chapters titled “Examination of Rank-Classes” were also collected in other administrative compendia, especially of the Ministry of Personnel, and circulated as separate booklets (<cite id="betaf"><a href="#zotero%7C14298532%2FMNBH9DQS">(Will, 2020)</a></cite>, 120-121. Our translation of the title is more literal than Will’s, because we wanted to highlight the emphasis on the system of numeric rank-classes.
). The goal of these regulations was to create a rational and stable framework that limits arbitrary acts arising from patronage relationships (<cite id="pybej"><a href="#zotero%7C14298532%2F9XED7GPL">(S. 吴思 Wu, 2009)</a></cite>, 255). Given that *Mandarin Promotions* has been mistaken for an “official directory,” it is necessary to bring in such an official bureaucratic promotion chart for comparison.

<!-- #endregion -->

### Official Rules: The Examination of Rank-Classes

<!-- #region citation-manager={"citations": {"gnysg": [{"id": "14298532/MNBH9DQS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The “Examination of Rank-Classes” (below “Examination”) contains a list of over 200 official designations which are arranged by their assigned rank-class from the highest rank-class to the lowest. There were 9 ranks (*pin* 品) with 18 classes (*ji* 級), hence “*pinji*,” plus one unclassed (*weiruliu* 未入流), making 19 which are habitually numbered 1a to 9b, plus “unclassed” (10 in our encoding). More importantly, the “Examination of Rank-Classes” also contains orderly steps from lower ranks up to higher ranks. In other words, each office can only be recruited from a limited number of lower-ranking offices and be appointed to a limited number of higher-ranking offices. The foremost student of the Qing administration outside China, Pierre-Étienne Will, has observed that “the same content is also found in … tables called Shengguan tu 陞官圖, Baiguan duo 百官鐸, and other names, that were popular from the Ming through the Republican periods (and were adapted in Japan taking account of local institutions), and served as a support for a game played with dice” (<cite id="gnysg"><a href="#zotero%7C14298532%2FMNBH9DQS">(Will, 2020)</a></cite>, 121). In other words, the “Examination” was the ideal material for gamification. So, how is *Mandarin Promotions* related to these chapters?

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0gypl": [{"id": "14298532/SYYWS26A", "source": "zotero"}], "rmtb4": [{"id": "14298532/MGTNKIZA", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
As a proof of concept, we may use a network to inspect an “Examination” chapter. The *Collected Statutes* were updated from time to time, so there are five editions throughout the Qing. The editions closest to 1840 were printed in 1768 and 1823 (<cite id="rmtb4"><a href="#zotero%7C14298532%2FMGTNKIZA">(Wilkinson, 2012)</a></cite>, 843). We have had only the edition of 1768 at hand, but research has shown that changes in “Examination” were slight (<cite id="0gypl"><a href="#zotero%7C14298532%2FSYYWS26A">(Y. 伍躍 Wu, 2022)</a></cite>). As we will see below, the big change also came in 1843, i.e. after the game chart was created, so this may be acceptable. Author A digitized this edition and compiled it into a source-target table, which she then entered into Gephi and analysed the graph by applying modularity and betweenness centrality algorithms. This procedure yielded the following graph:

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-321-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Examination of Rank-Classes"
            ]
        }
    }
}
display(Image("media/Figure 3.2.1. PJK_chin.png"), metadata=metadata)
```

<!-- #region citation-manager={"citations": {"s1zfn": [{"id": "14298532/WB58FURK", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
This graph first shows a high degree of modularity which is not a fact widely known about the Qing bureaucracy.  Modularity (or community detection) is defined as “decomposing the networks into sub-units or communities, which are sets of highly interconnected nodes” (<cite id="s1zfn"><a href="#zotero%7C14298532%2FWB58FURK">(Blondel et al., 2008)</a></cite>, 2). We may remind the reader that this is not a social network. Clustered areas do not mean that officials of these types socialized more with each other than with others. Rather, as in a transport network, communities show areas more densely connected by career paths and distinguish them from other areas which are more distantly connected. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"h12lj": [{"id": "14298532/BMQLXB3T", "source": "zotero"}], "kfkkh": [{"id": "14298532/6A3DYQPG", "source": "zotero"}]}} -->
The graph actually shows that low-ranking provincial bureaucrats are clustered in the lower corner (black), worlds apart from an isolated upper-level court bureaucracy in the capital Beijing (purple, upper right). A reference to the actual officialdom is necessary here. The names of all appointed officials were listed in quarterly official directories (*jinshenlu* 縉紳錄) and published four times every year. These official directories have now been compiled into the Chinese Government Employee Database-Qing (CGED-Q) by the Lee-Campbell group. Chen Bijia’s research on these data has shown that Beijing’s bureaucracy was staffed quite differently from the provincial bureaucracies, one consisting predominantly of Manchus and Examination candidates, the other crowded by Han officials and office purchasers (<cite id="kfkkh"><a href="#zotero%7C14298532%2F6A3DYQPG">(Chen, 2019)</a></cite>. For the database: <cite id="h12lj"><a href="#zotero%7C14298532%2FBMQLXB3T">(Chen et al., 2020)</a></cite>). Now we can confidently argue that this difference was related to the systematic setup of the statutory system.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"9wum6": [{"id": "14298532/LC5FSDKM", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We also see that certain positions have a higher centrality than others. There are many types of centralities. In accordance with our metaphor of a transport network, we chose betweenness centrality as the defining indicator of the importance of a node, because it measures the number of shortest paths that pass through a node. “Betweenness Centrality is [also] a way of detecting the amount of influence a node has over the flow of information or resources in a graph. It is typically used to find nodes that serve as a bridge from one part of a graph to another” (<cite id="9wum6"><a href="#zotero%7C14298532%2FLC5FSDKM">(Needham &#38; Hodler, 2019)</a></cite>, 97). In our projection, these positions were major hubs and bridges between distinct segments of the rank system. Hence, they can be considered pivotal for the career of officials. Betweenness centralities are clearly linking  communities, with the county magistrate (*zhixian* 知縣, 7a)  having the highest centrality between low- and mid-level positions, while the vice department director (*yuanwailang* 員外郎) and investigating censor (*jiancha yushi* 監察御史), both rank-class 5b, link to the higher court offices in the capital. 

<!-- #endregion -->

Theoretically, comparing centralities could help to evaluate the faithfulness of *Mandarin Promotions* to official regulations. Unfortunately, this proved impractical. To be sure, all office designations listed on the game chart do exist in various bureaucratic regulations of the Qing with exactly the correct names. However, they nowhere exist in the same combination.


<!-- #region citation-manager={"citations": {"ochlz": [{"id": "14298532/JDFA84RJ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
First, “Examination” alone came in four versions for various ethnic status groups in the Qing bureaucracy: Han, Manchu, Mongols, and Han bannermen (for these status distinctions see: <cite id="ochlz"><a href="#zotero%7C14298532%2FJDFA84RJ">(Porter, 2023)</a></cite>). The game designer, by contrast, combined the Han and Manchu. Secondly, the “Examination” chapters contain only ranked offices and the paths between them. They are comparatively simple. *Mandarin Promotions*, by contrast, contains official posts, but also the important *chushen* provenances ( ”Examination“ chapters do contain a few chushen provenances, but not systematically.
), examinations, temporary commissions, honorific titles and titles of nobility, and even imperial rewards and baubles. The game creates additional suspense by letting players pass through the hoops of a simulated review process, getting promotions for excellence and demotions for failures. As a result, there are many more positions in the game than in any of the four “Examination” chapters. Thirdly, the game chart overrepresents metropolitan offices (i.e. those in the Imperial and Court administration located in Beijing). More precisely, these offices are more differentiated than in “Examination.” For example, the county magistrate distinguishes “busy” and “simple” counties. The differentiation is even more pronounced in the metropolitan offices. A concrete example from the Six Ministries will be shown below in subsection [3.4](#subsection-3.4). As a result, provincial offices have a higher mathematical centrality in the complete graph. Fourthly, the game designer had to be concerned with symmetry. Since the game was played by dice, each position has only six options for the next step, in network-speak it has an out-degree of at most 6. This was different from real promotion options, of course. Finally, results may be skewed due to decisions made by the researcher when she set up the data model, most prominently the inclusion of a Commoner position outside the game chart, before the player obtains a *chushen* with their first roll of dice, as well as the final positions, which only reckon the rank-class of the last position a player held by the end of the game. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The following graph plots modularity (color) and betweenness centrality (size of label) in Mandarin Promotions, in a similar way as [2](#figure-321-*) did for the “Examination” chapter. To avoid the hairball effect, the graph is filtered by cutting out nodes with extremely high (the Commoner) and low (most if not all of the temporary nodes, the remaining ones are nameless—NA—in the graph) betweenness centrality. As the previous graph, this one, too, is produced in Gephi using the projection Force Atlas.

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-322-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Mandarin Promotions (Modularity and Betweenness Centrality)"
            ]
        }
    }
}
display(Image("media/Figure 3.2.2. SGT v.4 filtered chin.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
As discussed above, the greater differentiation of positions creates very different centralities.  We cannot expect to replicate the results of the “Examination.” Provincial positions have a much higher centrality, especially the Provincial Surveillance Commissioner (P140, *anchashi* 按察使, rank-class 3a) and the two prefects (*zhifu* 知府, 5b, busy and simple P117, P118). 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
However, we do see interesting parallels to “Examination”. One is the clustering of low-ranking provincial officials at the bottom as well as the clustering of high-ranking court offices in Beijing at the other end. Metropolitan offices also form other isolated clusters: In green what I term the “Academe” where graduates of the highest of three levels of the civil service examinations clustered together in an arch that offered direct access to high-ranking office both in the provinces (Provincial Governor, 2a) and in the capital (Right Vice Minister of Rites, 2a, the Ministry of Rights was reserved for examination graduates, see below). A further cluster can be seen in the grey arch opposite the lower curve. These are entirely Manchu positions (not included in the Han-only version of “Examination”). 

<!-- #endregion -->

Finally, in both “Examination” and Mandarin Promotions we find two isolated cul-du-sac careers. These are the Royal Directorate of Astronomy (C40, *qintianjian* 欽天監) and the Imperial Academy of Medicine (C39, *taiyiyuan* 太醫院). In the game, students of astronomy and medicine were the most undesirable chushen starting positions. Original rules on the 1840 game chart stipulated that players landing on these positions should rather seek to bail themselves out by purchase. This is an expression of a value system that cherishes noble status and examination virtue over professional work. 



### Realism: The Case of Prefects


<!-- #region citation-manager={"citations": {"20tnm": [{"id": "14298532/LC5FSDKM", "source": "zotero"}]}} -->
In network terms, the above explorations are  “graph-global” questions, pertaining to properties of single nodes in relation to the entire graph. More comparisons are possible if we turn to what would be termed “graph-local” questions in network terms, that is, investigation of properties that are calculated based on a neighborhood of each node (<cite id="20tnm"><a href="#zotero%7C14298532%2FLC5FSDKM">(Needham &#38; Hodler, 2019)</a></cite>, 6). Here, we attempt only two. First, we could show how faithfully the promotion rules in the game mimic the statutory promotion rules in “Examination”. Secondly, we will turn to the dice values which accompany the promotions in the game to gauge the value judgement of the game designer.

<!-- #endregion -->

For the first question, we examine the case of prefect as an example. This has two reasons. First, the prefect has a relatively high centrality in the game (see graph above). Secondly, there has been a scholarly debate about the prefects lately.  The debate is relevant for our argument because it shows that, while the game certainly does not reflect reality, the statutory system of the Qing, for which the “Examination of Rank-Classes” stand as proxies, did not perform much better. It was by itself an “utopia of rules.” Reality on the ground looked very differently. 


<!-- #region citation-manager={"citations": {"95i0u": [{"id": "14298532/3TJV8LU6", "source": "zotero"}]}} -->
In the Qing administrative system, the prefecture is a unit of territorial administration that is between the county and the province. A prefecture has several counties, and a province has several prefectures. Appointments to prefect positions were the subject of a recent study by Hu Heng et al. which is part of the growing body of research that is being produced out of the Chinese Government Employee Database-Qing (CGED-Q, <cite id="95i0u"><a href="#zotero%7C14298532%2F3TJV8LU6">(Hu et al., 2020)</a></cite>). Hu Heng et al. focus on appointment procedures in the appointments of 3,403 prefects in CGED-Q (1833-1911). Prefectures  had designations of importance, namely as “most important” (*zuiyao* 最要), “important” (*yao* 要), and “simple” (*jian* 簡). They also had designations of appointment prerogative, namely: 1. appointment by imperial edict (*qingzhi que* 請旨缺, 48.3% of vacancies); 2. appointment upon request of the governor (*tidiao que* 題調缺, 26.1.% of vacancies); 3. appointment by Board of Personnel (*buxuan que* 部選缺, 25.6% of vacancies). This makes prefectures a perfect case to discuss the balance of power between the court, the Ministry of Personnel, and the provincial governors. Hu argues (p. 368) that 43.3% of all vacancies (102) were to be appointed by imperial edict  (*qingzhi que* 請旨缺), and these were located in the most important, connected and wealthy places. This shows that the throne maintained centralized power over the appointment process, while the Board of Personnel was comparatively weak, finding its appointments infringed by both the throne and the governors. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"5oua1": [{"id": "14298532/SYYWS26A", "source": "zotero"}]}} -->
Wu Yue, one of the most exacting scholars of Qing institutional history, subsequently attacked these findings. He argued that the official directories were a bureaucratic fiction. More often than not, they reflect an abstract appointment to a rank with no guarantee that the candidate actually showed up on the ground (as he shows in detail, some never served in the position they were nominally appointed to). Wu also dampens the idea of a power struggle in the appointment designations. The appointment procedures were highly regulated, namely by the “Examination of Rank-Classes”. The only ways for the governors to break away from these procedures were those not expressed in the official directories, namely sending appointed prefects on commissions and temporary substitutions elsewhere, while filling the vacant posts with their own substitutes (<cite id="5oua1"><a href="#zotero%7C14298532%2FSYYWS26A">(Y. 伍躍 Wu, 2022)</a></cite>). 

<!-- #endregion -->

We could argue that a board game is fictional, because it does not represent the murky waters of provincial dealings. However, as Wu Yue has shown, the administrative laws of the empire did not perform more faithfully. Therefore, we feel confident that the comparison between the “Examination of Rank-Classes” and M*andarin Promotions* can yield meaningful results, without caring too much about its relationship with bureaucratic reality on the ground.  What we want to know is if the game replicates the “Examination” and which edition it was based on. 


<!-- #region editable=true slideshow={"slide_type": ""} -->
For this purpose, we examined who could be appointed to prefect in the game and found that the appointments in the game are consistent with the appointments in the 1768 edition of the “Examination,” except in a few cases that can easily be explained. The classifications of prefectures into degrees of importance (see above) were not listed in the “Examination” (its sources were in other regulations). *Mandarin Promotions*, on the other hand, expresses them in a simplified way by distinguishing only between “busy (i.e. lucrative) prefecture” (*fanfu* 煩府, P117) vs. “simple prefecture” (*jianfu* 簡府, P 118). This procedure is the same as for counties mentioned above. The table below contains appointments to both “busy” and “simple prefecture” for Mandarin Promotions.

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Appointments to Prefect in \u201cExaminations\u201d and Mandarin Promotions"], "type": "image"}} slideshow={"slide_type": ""} tags=["table-32-*"] -->
|Examination of Rank-Classes (Han, 1768)|Mandarin Promotions|Translation (Explanation)
|---|---|---
||C14-捐班候補 : P86-候補府|Expectant prefect 
|直隸州知州|C17-直隸州 : P109-知州|Department Magistrate of an Independent Zhou-Department
|府同知|C18-直隸廳 : P113-同知|Vice Prefect of an Independent Ting-Department 
||C19-外府 : P119-同知|Vice Prefect in a Subprefecture outside the capital 
||C20-京府 : P130-四路同知|Vice Prefect in a capital prefecture (Shuntian or Fengtian)
||C25-河院 : P163-同知|Vice Prefect of Grand Canal Administration
|順天府治中|C20-京府 : P129-治中|Deputy Vice Governor of Shuntian Prefecture
|奉天府治中||Deputy Vice Governor of Fengtian Prefecture
|各省鹽運司運同|C24-鹽院 : P154-運同|Deputy Salt Controller
|六部郎中|C32-工部 : P193-郎中|Department Director in one of the Six Ministries (MP: Ministry of Works)
||C33-刑部 : P201-郎中|Ditto, Ministry of Punishments
||C34-兵部 : P209-郎中|Ditto, Ministry of War
||C35-禮部 : P216-郎中|Ditto, Ministry of Rites
||C36-戶部 : P226-郎中|Ditto, Ministry of Revenue
||C37-吏部 : P234-郎中|Ditto, Ministry of Personnel
|六部員外郎|C32-工部 : P194-員外|Vice Department Director in one of the Six Ministries (MP) Ministry of Works
||C33-刑部 : P202-員外|Ditto, Ministry of Punishments
||C34-兵部 : P210-員外|Ditto, Ministry of War
||C35-禮部 : P217-員外|Ditto, Ministry of Rites
||C36-戶部 : P227-員外|Ditto, Ministry of Revenue
||C37-吏部 : P235-員外|Ditto, Ministry of Personnel
||C48-會同四譯館 : P302-郎中|Chief Minister of Interpreters and Translators Institute (in fact, also a “department director” by rank)
||C51-理藩院 : P316-郎中|Department Director in Court of Colonial Affairs


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Here we see, that in some cases “Examination” is more specific, for example in C20-P129 where the Pinjikao distinguishes between two different capitals, the actual capital Beijing (Shuntian prefecture) and the Manchu capital Shengjing, todays Shenyang (Fengtian). In other cases, there is a lacuna in “Examination.” C48 and C51 are Manchu institutions where positions are reserved for Manchu officials, hence they are missing in the Han-only “Examination” table used for this comparison. Often, *Mandarin Promotions* is much more detailed, as in the Ministries. More on those below. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0idrm": [{"id": "14298532/B4NHBRJH", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The most interesting difference is in the existence of the independent Ting-department (as opposed to Zhou-department). “Independent” means that the department (a sort of county) is not governed by a country magistrate (*zhixian* 知縣, rank-class 7a). The governing official of an independent department (*zhilizhou* 直隸州) is a department magistrate (*zhizhou* 知州, rank-class 5a), which is three classes (*ji*) higher than a magistrate, and he directly answers the governor of a province, not a prefect. The ting was a peculiar administrative unit where a prefect sent one of his two vice-prefects (*tongzhi* 同知 or *tongpan* 通判) to take direct control of an area which was often located strategically important border regions and ruled by local tribes. Hu Heng has shown that the institutionalization of the ting did not happen before the mid eighteenth century and was due to the Qianlong’s decision in 1741 to never again increase the number of statutory officials to save government expenditures. The ossification of the imperial bureaucracy then mostly forestalled further administrative expansion and resulted in the non-conventional use of auxiliary officials for functions previously reserved to seal-holding officials, namely taxation and law. The Collected Statutes reflected the change with a time lag, and the ting officials (*zhiliting tongzhi* 直隸廳同知, *zhiliting tongpan* 直隸廳通判) first showed up in the 1822 edition (<cite id="0idrm"><a href="#zotero%7C14298532%2FB4NHBRJH">(Hu, 2013)</a></cite>). However, even though the ting was mentioned in other parts of the expansive collection, it was never included in the “Examination” chapters (even in the 1886 edition). This shows that our version of *Mandarin Promotions* was designed in the early 19th century, that is, the date of 1840 on the preface of the earliest known version of this particular civil-official game board was the genuine date of creation. It also shows that the designer used the full extent of the Collected Statutes instead of simply gamifying the “Examination” table.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"xc66g": [{"id": "14298532/3TJV8LU6", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
What did prefect appointments really look like on the ground? Hu Heng et al have produced a statistics of 2,471 prefects for whom the previous position is known (<cite id="xc66g"><a href="#zotero%7C14298532%2F3TJV8LU6">(Hu et al., 2020)</a></cite>, 381-382). If we rearrange the table a little, the breakdown looks like [4](#figure-prefect-origins-*).

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-prefect-origins-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Previous Positions of Prefects"
            ]
        }
    }
}
display(Image("media/Figure 3.2.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
In this chart, we find two differences from the regulations listed above. Among unexpected candidates for prefects were, firstly, those that we have termed the “Academe” and the “Censorate.” These were positions reserved for graduates of the civil service examinations. Together, they received at least 24% of all appointments. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"29num": [{"id": "14298532/WSGVR2JV", "source": "zotero"}], "7pqrb": [{"id": "14298532/DGARYT8Z", "source": "zotero"}], "dduno": [{"id": "14298532/T57KB3SN", "source": "zotero"}], "ehq8l": [{"id": "14298532/RIQ5GUEC", "source": "zotero"}], "lel0m": [{"id": "14298532/SYYWS26A", "source": "zotero"}], "qdqyk": [{"id": "14298532/S78TH7KN", "source": "zotero"}], "v4f64": [{"id": "14298532/IVZDEUYV", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The Investigating Censor (rank-class 5b) was a pivotal position, and, hence, has a high centrality in the “Examination” of 1768 (figure [2](figure-321-*)). According to Wu Yue, the promotion path of censors changed only in 1843, in one of the few major revisions in the “Examination” chapters (<cite id="lel0m"><a href="#zotero%7C14298532%2FSYYWS26A">(Y. 伍躍 Wu, 2022)</a></cite>, 37-39. This revision was published as part of the Regulations of the Ministry of Personnel. <cite id="v4f64"><a href="#zotero%7C14298532%2FIVZDEUYV">(Libu, 1969)</a></cite>, Facsimile of the 1843 edition). Before this change, the Investigating Censor (rank-class 5b) could be appointed Circuit Intendant (4a), which was a major promotion in rank-class. After this change, the Investigating Censor could only be promoted to Prefect (4b), which appears as a depreciation in rank, but offered more opportunities for provincial appointment, because there were more prefectural positions. Since the throne, as we have seen above, had a say in the appointment process, appointing examination graduates from the metropolitan Academe and Censorate, provided one of the rare channels of mobility between the metropolitan and provincial bureaucracies, and gave some career advantage to examination graduates (“regular path”) against purchasers (“irregular path”). Peng Peng’s statistics (<cite id="ehq8l"><a href="#zotero%7C14298532%2FRIQ5GUEC">(Peng, 2022)</a></cite>, 154-155), although incomplete for the nineteenth century, corroborate this impression. They show that in relative terms the ratio of purchasers in prefects did not rise, although it did rise in the population of county magistrates as Kondo and Marsh had shown previously (<cite id="dduno"><a href="#zotero%7C14298532%2FT57KB3SN">(Marsh, 1962)</a></cite>; <cite id="qdqyk"><a href="#zotero%7C14298532%2FS78TH7KN">(Kondō, 1963)</a></cite>; <cite id="29num"><a href="#zotero%7C14298532%2FWSGVR2JV">(Kondō, 1963b)</a></cite>, <cite id="7pqrb"><a href="#zotero%7C14298532%2FDGARYT8Z">(Kondō, 1963c)</a></cite>). 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"luvqs": [{"id": "14298532/SYYWS26A", "source": "zotero"}], "r8j3c": [{"id": "14298532/7QCP8KGW", "source": "zotero"}]}} -->
The second unexpected candidate for prefect was the county magistrates (*zhixian* 知縣, 7a). Wu Yue has criticized the study by Hu Heng et al., because his statistic lists the appointment of 135 county magistrates (*zhixian*) to prefect positions. Since their rank is 7a, the promotion would jump 5 steps in the ladder of rank-classes, to be appointed prefect (4b). This was impossible. The only way to circumvent the regulations in the “Examination of Rank-classes” would have been a special edict (i.e. extraordinary imperial patronage) or perhaps purchase (<cite id="luvqs"><a href="#zotero%7C14298532%2FSYYWS26A">(Y. 伍躍 Wu, 2022)</a></cite>, 37-47). On the other hand, in writing the biography of Li Hu 李湖 (1715- 1785), Kent Guy also claimed that a county magistrate could be directly appointed as prefect (<cite id="r8j3c"><a href="#zotero%7C14298532%2F7QCP8KGW">(Guy, 2014)</a></cite>, 81). How would the game behave?

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"lseb7": [{"id": "14298532/CTD5EWCD", "source": "zotero"}], "shyvi": [{"id": "14298532/CTD5EWCD", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We have already seen that *Mandarin Promotions* follows the “Examination of Rank-Classes” and did not allow a direct career move from county magistrate to prefect. Plotting *Mandarin Promotions* as a network graph allows us to examine longer paths. The game also simulates the results of triennial performance reviews called Great Reckoning (*daji* 大計, <cite id="lseb7"><a href="#zotero%7C14298532%2FCTD5EWCD">(Hucker, 1985)</a></cite>, no. 5891) in the provinces and Capital Evaluation (*jingcha* 京察, <cite id="shyvi"><a href="#zotero%7C14298532%2FCTD5EWCD">(Hucker, 1985)</a></cite>, no. 1189). The only way in *Mandarin Promotions* to be promoted from county magistrate to prefect within two rounds of dice, i.e. not going through another ranked position,  was through an outstanding performance review judged as either “*zhuoyi* 卓異” (outstanding) or “*nei jiming* 內記名” (royal nomination).

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-33-*"] -->
|County Magistrate|Great Reckoning verdict|Appointed to
|-|-|-
|C15-縣 : P92-京縣 County Magistrate in the Capital Prefecture|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a difficult prefecture
|C15-縣 : P93-煩縣 County Magistrate in a difficult county|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a difficult prefecture
|C15-縣 : P94-簡縣 County Magistrate in a simple county|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a difficult prefecture



<!-- #endregion -->

<!-- #region citation-manager={"citations": {"gcsju": [{"id": "14298532/7QCP8KGW", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In addition, the rules of the game also allow purchase at the price of 5 chips per rank-class (ji). In other words, the game behaves exactly as Wu Yue would have predicted. In order to be appointed prefect, a magistrate would need a special imperial edict or to purchase the higher rank. There was no regular promotion from magistrate to prefect. As a matter of fact, Kent Guy writes about Li Hu, whose biography he studied: “When the post of prefect of Tai'an became vacant, the fact was reported to the emperor who then chose the new appointee from among the officials known to him” (<cite id="gcsju"><a href="#zotero%7C14298532%2F7QCP8KGW">(Guy, 2014)</a></cite>, 81). This almost exactly describes the procedure which the game refers to as “royal nomination.” Following an outstanding review (or with sufficient patronage), an official could be added to a list of nominees from which the emperor would choose for extraordinary promotion, i.e. promotions that broke the confines of the “Examination of Rank-Classes.”

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
So, what does the case of prefect tell us about the game *Mandarin Promotions*? As a reminder, we study a post-1870s version of the game which is based on the 1840 original. First, the game is faithful to the statutory regulations of official promotion charts to a surprising degree, notwithstanding necessary abstraction in the performance review process. Secondly, the regulations that the game is based on are those before 1843. Thirdly, the post-1870s version did not revise the original setup to make it closer to current practice. This means that, because the game design did not change with the times, its level of abstraction increased, not because the game became more abstract, but because reality moved away. The same, though, as we have seen above, can be said for many of the Qing regulations themselves. As Wu Yue has shown, the statutory regulations themselves are not necessarily more “true” when it comes to the situation on the ground. For example, the *ting* department, albeit securely institutionalized, was not included in the “Examination of Rank-Classes.” Regulations create their own “utopia of rules.” What was in the regulations and what happened on the ground were two different things. Hence, the question of realism remains a tricky one. What reality shall we refer to?

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["subsection-3.4"] -->
### Value: The Case of Ministries
<!-- #endregion -->

As we have argued above, all designations listed on the game chart do exist in the bureaucratic regulations of the Qing. However, nowhere in the same combination. We can use this fact to gauge the perception of the game designer. How can deviations from the regulations inform us about his value system? 

<!-- #region editable=true slideshow={"slide_type": ""} -->
One example is the distribution of the Six Ministries in Beijing. They are Public Works (C32), Punishments (C33), War (C34), Rites (C35), Revenue (C36), and Personnel (C37), and all have similar positions, namely:
- *Shangshu* 尚書, 1b, Minister
- *Zuo Shilang* 左侍郎, 2a, Left Vice Minister 
- *You Shilang* 右侍郎, 2a, Right Vice Minister
- *Langzhong* 郎中, 5a, Department Director
- *Yuanwailang* 員外郎, 5b, Vice Department Director
- *Zhushi* 主事, 6a, Secretary 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The “Examination” chapters distinguish only between the Ministry of Personnel and the rest, and treat most promotions equally, not specific to the ministry, except that the Ministry of Rites was reserved for candidates with examination degrees. Hence, it is easy to calculate the centrality of certain positions. We find that the vice department director is the position with the highest betweenness centrality (see [2](#figure-321-*)). 
<!-- #endregion -->

In *Mandarin Promotions*, each ministry is listed with its full list of positions. In general, Beijing positions are overrepresented and more differentiated. Due to their duplication across ministries, we cannot determine the centrality of certain official ranks in general. For instance, we cannot say if the vice department director has the same centrality in the game as in “Examination”, because in the former that position exists in more than one ministry. However, we can determine whether the game designer assigned special interest to certain ministries and certain positions. 

<!-- #region editable=true slideshow={"slide_type": ""} -->
For this, we again turn to a graph-local question and use the in-degree of the three lower-ranking positions in each ministry. We remind the reader that the game designer has attached value to dice rolls by naming them, namely: <span style="font-variant: small-caps;">virtue</span> (44), <span style="font-variant: small-caps;">talent</span> (66), <span style="font-variant: small-caps;">effort</span> (55), <span style="font-variant: small-caps;">mediocre</span> (33), <span style="font-variant: small-caps;">weak</span> (22), <span style="font-variant: small-caps;">corrput</span> (11). We argue that these names are meaningful and imbue the result of the dice roll with moral value. In a way, they return meritocratic (hence competitive, agon) value to the game, which is entirely a game of luck (alea). We can, therefore, assign a “merit score” by calculating the in-degree by edge type. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
On the surface, the distribution of merit scores between the six ministries appears evenly distributed with peaks of a higher number of incoming edges in the Ministries of Revenue and Punishments. That there are fewer candidates appointed with a corrupt verdict is natural. Firstly, there are fewer “corrupt” scores in the entire graph. Among the <span style="font-variant: small-caps;">merit</span> relationships, 3,687 are for <span style="font-variant: small-caps;">virtue</span>, 3,868 <span style="font-variant: small-caps;">talent</span>, 3,404 <span style="font-variant: small-caps;">effort</span>, 3,139 <span style="font-variant: small-caps;">mediocre</span>, 2,861 <span style="font-variant: small-caps;">weak</span>, and only 1,064 <span style="font-variant: small-caps;">corrput</span>. The general sentiment of the game, it appears, is one of optimism. Secondly, if a “corrupt” score lands you on a position, this is mostly a demotion, i.e. a downgrading from higher rank. 
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-341-*"] -->
Merit|War|Works|Revenue|Rites|Punishments|Personnel|
-|-|-|-|-|-|-|
<span style="font-variant: small-caps;">virtue</span>|66|51|78|79|79|59
<span style="font-variant: small-caps;">talent</span>|49|58|76|51|73|49
<span style="font-variant: small-caps;">effort</span>|53|54|63|52|66|70
<span style="font-variant: small-caps;">mediocre</span>|60|59|72|45|51|48
<span style="font-variant: small-caps;">weak</span>|42|58|64|51|45|53
<span style="font-variant: small-caps;">corrupt</span>|12|15|14|23|11|14
Total In-degree|282|295|367|301|325|293


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
While virtue, talent, and effort should equally lead to success, the bias is also tilted towards virtue and talent, with the Ministries of Revenue, Punishment and Rites all strong in virtue, but only the former two are also strong in talent. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
This trend is more pronounced for the three entry-level positions in the ministries (i.e. those positions that could be directly purchased, see subsection [4.2](#subsection-4.2).) where the Ministries of Revenue, Punishments, and Works stand out.

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-342-*"] -->
||郎中, 5a, Department Director|員外郎, 5b, Vice Department Director|主事, 6a, Secretary|Totals
-|-|-|-|-
C32-Works|P193|P194|P195||
<span style="font-variant: small-caps;">effort</span>|4|19|11
<span style="font-variant: small-caps;">virtue</span>|4|19|4
<span style="font-variant: small-caps;">talent</span>|4|31|13
<span style="font-variant: small-caps;">weak</span>|4|18|16
<span style="font-variant: small-caps;">mediocre</span>|6|16|13
<span style="font-variant: small-caps;">corrupt</span>|3|3|6
Total In-degree|25|106|63|194
|||||
C33-Punishments|P201|P202|P203
<span style="font-variant: small-caps;">effort</span>|8|22|12
<span style="font-variant: small-caps;">virtue</span>|6|26|14
<span style="font-variant: small-caps;">talent</span>|10|28|14
<span style="font-variant: small-caps;">weak</span>|4|10|9
<span style="font-variant: small-caps;">mediocre</span>|5|12|8
<span style="font-variant: small-caps;">corrupt</span>|1|4|5
Total In-degree|34|102|62|198
|
C34-War|P209|P210|P211
<span style="font-variant: small-caps;">effort</span>|11|14|5
<span style="font-variant: small-caps;">virtue</span>|11|12|5
<span style="font-variant: small-caps;">talent</span>|11|8|6
<span style="font-variant: small-caps;">weak</span>|6|7|5
<span style="font-variant: small-caps;">mediocre</span>|10|8|7
<span style="font-variant: small-caps;">corrupt</span>|1|3|5
Total In-degree|50|52|33|135
|
C35-Rites|P216|P217|P218
<span style="font-variant: small-caps;">effort</span>|8|10|17
<span style="font-variant: small-caps;">virtue</span>|14|9|9
<span style="font-variant: small-caps;">talent</span>|14|8|10
<span style="font-variant: small-caps;">weak</span>|8|3|17
<span style="font-variant: small-caps;">mediocre</span>|7|4|11
<span style="font-variant: small-caps;">corrupt</span>|4|3|6
Total In-degree|55|37|70|162
|
C36-Revenue|P226|P227|P228
<span style="font-variant: small-caps;">effort</span>|10|17|22
<span style="font-variant: small-caps;">virtue</span>|11|15|14
<span style="font-variant: small-caps;">talent</span>|10|16|33
<span style="font-variant: small-caps;">weak</span>|8|13|22
<span style="font-variant: small-caps;">mediocre</span>|7|8|21
<span style="font-variant: small-caps;">corrupt</span>|2|2|5
Total In-degree|48|71|117|236
|
C37-Personnel|P234|P235|P236
<span style="font-variant: small-caps;">effort</span>|8|18|14
<span style="font-variant: small-caps;">virtue</span>|13|14|10
<span style="font-variant: small-caps;">talent</span>|12|15|10
<span style="font-variant: small-caps;">weak</span>|5|9|12
<span style="font-variant: small-caps;">mediocre</span>|5|6|12
<span style="font-variant: small-caps;">corrupt</span>|1|4|3
Total In-degree|44|66|61|171


<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-342-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Examination of Rank-Classes"
            ]
        }
    }
}
display(Image("media/Figure 3.4.2. Merit_Scores_RadarChart_en.png"), metadata=metadata)
```

<!-- #region citation-manager={"citations": {"4buyp": [{"id": "14298532/PX4XEZRW", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
This balancing between virtue and talent is not self-explanatory. In the nineteenth century, there was a debate about whether virtue or talent was more important for official appointments. The reason was that it gradually dawned on decision makers that the old examinations with their heavy emphasis on the Confucian classics (virtue) no longer sufficed to solve real-world problems. Defenders of office selling, on the other hand, argued that to open this path could attract practical talent (One example comes from Wang Kaiyun 王闓運 (1833-1916): “Men who obtain office by purchase are one third less than those who obtain office by recommendation for military merit, but their talents and administrative abilities are often better than those of magistrates with regular qualification (*zhengtu*). Therefore, though it is true that office purchase is harmful to politics, the allegation that it is responsible for spoiling bureaucratic ranks is not necessarily true.” See: <cite id="4buyp"><a href="#zotero%7C14298532%2FPX4XEZRW">(Wang, 1983)</a></cite>, 165). The Ministries of Revenue, Punishments and Works were popular among office purchasers, and the three positions listed above were those accessible by purchase. The game designer’s “hidden” bias seems clear. This may also be expressed in the lower “popularity” (and tilt towards <span style="font-variant: small-caps;">weak</span>) of the Ministry of Rites, the old refuge of examination graduates.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"q3d5g": [{"id": "14298532/LADB2N7R", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
These three tests are limited in scope, but readers can feel free to make more tests using the data. In summary, they show that, first, *Mandarin Promotions* can be used to teach the actual operation of the Qing bureaucracy, albeit only the statutory one. Secondly, we can also confidently use the game to understand how the game designer (or game designers, as there were additions in later versions) perceived the Qing bureaucracy of his (their) time. We will turn, in the following section, to the question of how the game perceived the idea of meritocracy and equal opportunity, which has been the assumed guiding principle of the Qing bureaucracy since it first became known in Europe during the seventeenth century (<cite id="q3d5g"><a href="#zotero%7C14298532%2FLADB2N7R">(Kaske, 2024)</a></cite>).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-4"] -->
## Equal opportunity? Do all players have a chance to win?
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### *Chushen*
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"v2s3p": [{"id": "14298532/F8METVWQ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Chushen provenances are the most neglected element of Qing social life. Historically, having chushen (provenance) was the central precondition for any entry into the ranks of officialdom (Oddly, the term has been revived by Mao Zedong in the 1950s to denote hereditary class background. See: <cite id="v2s3p"><a href="#zotero%7C14298532%2FF8METVWQ">(Xu, 2021)</a></cite>). Scholars have long thought that the term “*chushen*” was simply a generic name for success in the civil service examinations. In fact, it denominates a much more diversified dividing line within the imperial status order, namely between commoner status and official status (independent of actual employment). Official rank denominated eligibility for occupying a certain position, the right to wear a certain gown, and a place in the overall hierarchy of enfranchised notables. 

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0o7xs": [{"id": "14298532/J8BBF2K4", "source": "zotero"}]}} -->
In the game, too, commoners (*baiding* 白丁) have no place.  They remain “outside the game” (*juwai* 局外, a term still used to describe outsiders in general), until fortune (the initial roll of dice) gives them chushen provenance. Fifteen of the chushen positions are in a department on the gameboard itself labelled “*chushen* 出身” (C1). Each of these fifteen denominations does have significance in the real world of the Qing dynasty. Other (real-world) *chushen* categories are in other departments of the game chart. Examination degrees beyond the first degree (P10, *shengyuan*), so-called “*kejia chushen* 科甲出身” are located in the departments for the provincial and metropolitan examinations. Hereditary titles of lower nobility listed below (C2) also conferred *chushen*, without being located in the “*Chushen*” department. Following the Taiping Rebellion (1850-1864) when so many officials perished in office, such titles were given to a son as a reward (<cite id="0o7xs"><a href="#zotero%7C14298532%2FJ8BBF2K4">(Meyer-Fong, 2013)</a></cite>). In the game they represent a big win. 

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-41-*"] -->
Dice|Compartment|Position|Translation|Category
-|-|-|-|-
3456|C1-出身|P1-蔭生|Honorary Licentiate|Hereditary privilege
1144|C1-出身|P2-軍功|Military Merit|Patronage
DxDx|C1-出身|P3-貢生|Senior Licentiate, Tribute Student|Examination/Purchase
T4|C1-出身|P4-恩賞|Imperial Grant|Patronage/Royal grace
T5|C1-出身|P5-保舉|Recommendation|Patronage
T6|C1-出身|P6-詞科|Graduate of Grace Palace Examination|Examination/Royal Grace
T3|C1-出身|P7-筆帖式|Banner clerk|Hereditary privilege (Manchu)
T2|C1-出身|P8-天文生|Student of Astronomy|Incipient professionalism
T1|C1-出身|P9-醫士|Student of Medicine|Incipient professionalism
D4|C1-出身|P10-生員|Licentiate|Examination
D6|C1-出身|P11-監生|Imperial Academy Collegian|Examination/Purchase
D5|C1-出身|P12-官學生|Student of the Banner School|Hereditary privilege (Manchu)
D3|C1-出身|P13-供事|Senior Clerk|Incipient professionalism
D2|C1-出身|P14-吏員|Clerk|Incipient professionalism
D1|C1-出身|P15-童生|Student|Examination
4444|C2-世爵|P16-衍聖公|Sacred Prince (Heir of Confucius)|Hereditary privilege
6666|C2-世爵|P17-一等輕車都尉|First Commander of the Light Chariot Force|Hereditary privilege
5555|C2-世爵|P18-二等輕車都尉|Second Commander of the Light Chariot Force|Hereditary privilege
3333|C2-世爵|P19-三等輕車都尉|Third Commander of the Light Chariot Force|Hereditary privilege
2222|C2-世爵|P20-騎都尉|Senior Commander of the Cavalry|Hereditary privilege
1111|C2-世爵|P21-雲騎尉|Junior Commander of the Cavalry|Hereditary privilege

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Confining ourselves to the fifteen positions in the “Chushen” department alone, we can for analytical purposes distinguish roughly five types of provenances: examinations, heredity, patronage (including imperial grace), incipient professionalism, and finally purchase. The game designer added value judgement by attaching dice value to each of the positions. The game is played with four dice. In the following, dice values are abbreviated as D “double”, T “triple.” Triples are only recognized for the very first roll of dice which establishes *chushen*. Hereditary privilege catapults the player into office right away, hence it is attached to LUCK dice (see subsection [2.1](#subsection-2.1)). The worst dice (D1, corrupt) is the student (P15) who is trying to pass the notoriously difficult examinations for his first degree (which is attainable by D4, virtue). Incipient professionalism (lowly clerks and the astronomers-doctors) is also bad. However, did these starting positions still have the equal chances to get ahead in the game? It is a game, after all, which is only fun if it has an equal playing field, literally. This section will use a Monte Carlo simulation to find out. Before discussing the technical details of this, we will first introduce another aspect of the game that has the potential to drastically change the role of the *chushen*, namely the possibility to purchase official rank.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["subsection-4.2"] -->
### Purchase 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"fe2pn": [{"id": "14298532/BK2CS6TS", "source": "zotero"}], "phw6p": [{"id": "14298532/9YAWZZJ4", "source": "zotero"}]}} -->
In the life-world of the game designer, the legal sale of official rank and appointments was rampant. The institution goes back to the beginnings of the Chinese empire and certainly to the beginning of the Qing dynasty (<cite id="phw6p"><a href="#zotero%7C14298532%2F9YAWZZJ4">(L. Zhang, 2023)</a></cite>). However, during the latter half of the eighteenth century, the Qianlong emperor (r. 1736-1796) frowned upon the practice and rarely licensed office-selling campaigns. This changed after 1798. In the early nineteenth-century, office selling became a regular experience (<cite id="fe2pn"><a href="#zotero%7C14298532%2FBK2CS6TS">(Kaske, 2018)</a></cite>). The design of the 1840 version of Mandarin Promotions began to reflect this change and introduced office purchase as a new option.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"4nfdk": [{"id": "14298532/9YAWZZJ4", "source": "zotero"}], "ajl4j": [{"id": "14298532/ZH6Y34YM", "source": "zotero"}]}} -->
Office purchase is the only element that returns agency to this game which was otherwise entirely determined by chance. The written rules printed in the center of the 1840 Oxford board allow office purchase up to a certain rank, at a price of 5 chips per rank-class. The rank-limit (4a in the provinces and 5a in Beijing) fully complies to the laws governing legal office selling at the time. Modern recreations of the game in Hong Kong discourage or ban office selling, because it destroys the suspense of the game (Puk Wing Kin, the historian, encourages his readers to ban office purchase, even though he faithfully explains the original rules that allow it (p. 29). Pan Guosen who has made major changes to the game follows the Oxford chart and eliminates the 捐班候補 block (<cite id="ajl4j"><a href="#zotero%7C14298532%2FZH6Y34YM">(Pan, 2017)</a></cite>, 87-88). He still allows purchasing a reinstatement into previous office (*juanfu* 捐復) after a penalty dismissal (Ibid., p. 97)). However, for historians, the expansion of office purchase in the nineteenth century raises the question whether this move increased or lowered social mobility (<cite id="4nfdk"><a href="#zotero%7C14298532%2F9YAWZZJ4">(L. Zhang, 2023)</a></cite>, passim, argues that office purchase served to solidify status within extended lineages rather than fostering social mobility). For the game, the important question then is how the game designers viewed this question, that is, what impact does purchase have on the relative advantages of the different *chushen* positions?

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Few specifics concerning the procedure and advisability of office purchase were given on the 1840 game chart. Only two functions of office purchase are mentioned, namely to bail out from an undesirable starting position (*chushen*) or from a penalty dismissal. The most undesirable starting positions of all were students of astronomy and medicine, as seen above. Interestingly, the only two major changes in the written rules from the 1840 board to the later boards concerned the astronomers and doctors (One rule stipulated that office purchase for bailout was only allowed in the second round, that is immediately after the player had landed on the respective *chushen* position, but not at a later point. The other rule change excluded them from titles of nobility high up in their career, but only if they had missed the bailout and proceeded with the game.). They were now forced to bail out right after they landed on one of the two undesirable starting positions. One highly plausible interpretation of this change is a contradiction between the original intentions of the game designer and the practicality of enjoying the game. While the original game designer aimed for a complete representation of the bureaucratic system, later players wanted to prevent boring cul-du-sac “careers” and chose to ignore these positions. 

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-4.2-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Office Purchase"
            ]
        }
    }
}
display(Image("media/Figure 4.2.jpg"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Late nineteenth-century game boards also created a new category of “expectant officials by purchase”, C14 in our data model, a sort of holding for office purchasers before they were appointed, then again by dice, to full positions (Fig. 4.2.). The list of offices for sale is telling. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In the real world, these refer to so-called “seal-holding” positions, chief-executives with access to a seal of office and, in the province, also to a treasury. These positions were most coveted. In the game, we have the three ministerial positions in Beijing discussed in section 3.4.
- Langzhong 郎中, 5a, Department Director 
- Yuanwailang 員外郎, 5b, Vice Department Director
- Zhushi 主事, 6a, Secretary
In addition, there are four positions in the provincial bureaucracy:
- Dao 道, 4a, Circuit Intendant
- Zhifu 知府, 4b, Prefect
- Zhizhou 知州, 5b, Department Magistrate
- Zhixian 知縣, 7a, County Magistrate (There are two more categories, all non-seal-holding offices are lumped together as one category. The internship is a further waiting category accessed by unfavorable dice from the other expectant officials.)
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"c572h": [{"id": "14298532/3TJV8LU6", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The introduction of the holding category again mirrors reality where many office purchasers spent years or decades as expectant officials without getting an appointment. In Qing office selling, what was sold was official rank with eligibility to appointment, but not the position itself. Hu Heng cites a case of a certain Wang Buduan 汪步端 who was appointed prefect in 1906 at age 52. He had purchased the Imperial Academy Collegian (P11 *jiansheng* 監生) and the rank of deputy prefect (P119 *tongzhi* 同知, 5a) in 1864, at the age of 10. This is a non-seal-holding rank and therefore cheaper. In 1903, he again purchased a rank elevation to prefect, a seal-holding position, and a peacock-feather plume decoration (P413 *hualing* 花翎). In the meantime, he had served as expectant official in various temporary commissions, before he was finally recommended (C1-P5 *baoju* 保舉) and appointed to a vacancy after 42 years (Cited from: <cite id="c572h"><a href="#zotero%7C14298532%2F3TJV8LU6">(Hu et al., 2020)</a></cite>, 382-383).

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In game terms, on the other hand, introducing the holding category functioned as a limitation on office purchase. It gave a choice of attractive positions, but then let the players continue by dice. For the ministries, the choice made by the later game designer confirms the popularity ranking which we observed  in section 3.4.: virtue leads to the Ministry of Revenue, talent to the Ministry of Punishments, effort to the Ministry of Public Works.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"7zbxw": [{"id": "14298532/9YAWZZJ4", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Our simulation will try to determine under which circumstances purchase of one of the positions among the “expectant officials by purchase” would be beneficial, considering both the purchase price, set in the game as 5 chips per rank-class, and the resulting winning opportunities in terms of money received from the pool and other players. As we have seen in the example of Wang Budan above, purchase of office in the real world happened in several steps (for details, see <cite id="7zbxw"><a href="#zotero%7C14298532%2F9YAWZZJ4">(L. Zhang, 2023)</a></cite>). In principle, the player has the free choice to purchase at any stage of the game, as long as the target office is ranked higher than the position that is currently being held by the player. However, as we shall see below when discussing the results of the simulation, among competing players, it is beneficial to purchase office very early on, often directly from the starting position.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Since the overt game rules are incomplete, we had to introduce a few rules of our own in order to limit the number of possible scenarios. To maintain plausibility from the perspective of an informed nineteenth-century Chinese player, we tried to shape these rules based on our understanding of real-world office selling.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Firstly, special rules apply to P8 (Student of Astronomy) and P9 (Student of Medicine). As we have already stated above, they are forced to purchase instantly to bail out from their provenance. Once they have moved on from their starting position in their respective careers as astronomer or physician, game rules exclude them from further purchase.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Secondly, in the real Qing world, all office purchasers had to purchase the degree of Imperial Academy Collegian first. Therefore, we added a price for an Imperial Academy Collegian (C1-出身 : P11-監生) of 5 chips, that has to be purchased first by players wanting to purchase in the next step one of the positions from the “expectant officials by purchase”, unless they happen to already hold that position or any ranked position by dice roll.  Dice rules, written in small script under each header, treat P11 the same as the Licentiate (C1-出身 : P10-生員). They assume that he would continue towards higher examination glory. In our rules, if a player comes to P11 by dice or by purchase, he has the free choice whether to proceed according to dice rules, which stipulate continuing to the provincial examinations, or to purchase a position from the list in C14. The Licentiate P10, by contrast, has to purchase P11 before he is allowed to purchase office instead of embarking on the examination path, but he can get a discount (2 chips). This rule is also informed by real-world practice, where the purchase of P11 often served to skip the first competitive step in the three-step imperial examinations.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Thirdly, we have to clarify unclear or incomplete rules in the C14 department of office purchasers (Fig. 4.2.):
1. For the dice roll “corrupt” the rule is “stop appointment 停補”. We interpret this rule as being sent back to (C1-出身 : P11-監生).
2. There are two positions, P89 and P90, which do not refer to actual positions but to a category, namely auxiliary officials (*zuoza* 佐雜) as opposed to seal-holding officers with access to an official seal. Since these positions do not offer specific targets for outbound moves, in the simulation, players can choose from a list of eligible  positions of appropriate rank in either the capital or the provinces, depending on whether they come from P89 or P90.  When a player moves to these positions (P89 and P90) their previous rank is stored in a special variable. In their next turn, they can make a choice among all positions that satisfy the following three criteria: 1) the target position is listed on a predefined list of purchasable auxiliary position (to exclude seal-holding positions); 2) the rank of the target position is higher than the previous rank; 3) the position is in the correct location (Beijing for P89, Provinces for P90). The price of the purchase is then calculated based on the rank of the specific position they go to in the second turn.


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Technical Background: Monte Carlo and the Rules of Purchase
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Analysing the question of opportunities in the game, both with and without the presence of purchase, requires a technical setup that goes beyond the network approach used in the previous section. While, as we have seen, that approach can be used to gain insight into several aspects of its design, there are also some limitations that are hard to overcome. Specifically, there are mechanisms in the game that need to take into account the precise path that a player has taken before ending up in a certain position. First, to make accurate statements about monetary aspects of the game, each transaction with the pool or in between players has to be recorded. Secondly, there are a few special rules in the game that limit access to certain positions depending on the background of the player, that is, whether or not they ever held specific positions earlier in the game. While in theory, it would be possible to account for these in a network, by defining each state as a tuple similar to the approach for concurrentnodes (see section [2.3](#subsection-23)), in practice this would lead to an unacceptable blow-up in the state space.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"34kik": [{"id": "14298532/6RRN59QA", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Another possibility for the analysis of a game would be deriving a system of mathematical equations that give an explicit solution to the various probabilities that one might be interested in. This has been done e.g. for the Game of the Goose (<cite id="34kik"><a href="#zotero%7C14298532%2F6RRN59QA">(Groote et al., n.d.)</a></cite>). However, this method is already quite involved for the much simpler Game of the Goose without even taking monetary aspects into account. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Hence, we have decided to pursue a straightforward yet effective approach, using a Monte Carlo method. Monte Carlo methods have been used extensively to study systems that are too complex to derive an explicit solution. They work by simulating the system for a large number of times, such that by the Law of Large Numbers, the observed distribution of outcomes will converge to their expected values. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In practical terms, in order to conduct the Monte Carlo experiment, we implemented the rules of the game (including the provisions for purchase partly made up by us) in Python, using the existing data in the CSV data files as a basis. While the regular flow of the game was relatively easy to implement from the basic rules, the simulation becomes much more difficult when also considering special rules that only apply in certain circumstances, such as a few positions being restricted to persons coming from a particular background, or the game mechanisms for astronomers and physicians that are locked into their career path unless they immediately buy out of it. Furthermore, while the course of the game is mostly decided by the roll of the dice, there are a few elements of choice, especially the option to purchase an office, for which we had to decide on and implement realistic strategies of how players would behave when they have the opportunity to influence the run of the game. These will be described in detail in section [4.5](#section-4.5), after first discussing the issue of opportunities without purchase in the following sections.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-44"] -->
### Simulation Results without Purchase
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Using the implementation of the game in Python, it is easy to collect data about the properties of certain positions by having the computer repeatedly play out entire games. In each game, we record relevant events such as what (random) dice rolls the players made, to which positions they moved accordingly, and how much money they received. Since simulating the game without purchase is computationally speaking extremely easy, for the results in this section, 100,000 playthroughs with 4 players each were conducted. Since we are mostly interested in extrapolating from this to the expected fate of individual players, this gives 400,000 unique traces of individual playthroughs of single players.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
In the following, we want to use this data to analyze the different *chushen*. Since the simulation precisely follows the prescribed rules in assigning *chushen* positions according to dice rolls, in the collected data, the *chushen* positions that are associated with dice combinations that are more likely to occur are overrepresented, while other chushen are underrepresented. Hence, to have a meaningful analysis, it is important to conduct a  sufficient number of experiments so that even for unlikely starting positions there is enough data. Using the 100,000 simulations, the least visited first position is P16 with 403 visits.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In each playthrough, all players start – just as in the game – outside the game board as prescribed in the rules. Hence, in order to analyze the different chushen, we have to group playthroughs by the position that the player first arrived at. Then, the *chushen* can be compared with each other by taking in-group averages for the values we are interested in, which will be described below. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
First, we consider how long it takes players starting from different chushen to reach the end of the game, i.e. one of the retirement positions. Table [6](#table-441-*) shows the average number of hops until retirement for the different *chushen*. The average over all playthroughs in 100,000 simulations with four players is as high as 37 (sd: 12.3), being most heavily influenced by those *chushen* that one can obtain with a double, i.e. P10-P15, as these are more likely to occur. Observe that in the simulation, a move corresponds to one hop in the network. This is not exactly the same as a roll of dice, as some combinations will not lead to any change in the gameboard, while for others, the player can take multiple steps at once.

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-441-*"] -->
| Dice | Position | Translation | Average number of hops until retirement | Average effective money (From/to pool, From/to other players) | Average final rank (1a = 19, unclassed = 1) |
|------|----------|-------------|----------------------------------------|--------------------------------------------------------------|-------------------------------------------|
| 3456 | P1-蔭生 | Honorary Licentiate | 31.2 | 19.6 (-3.6, 23.3) | 17.9 |
| 1144 | P2-軍功 | Military Merit | 35.8 | -11.1 (-5.7, -5.4) | 17.7 |
| DxDx | P3-貢生 | Senior Licentiate, Tribute Student | 36.4 | 7.5 (0.2, 7.4) | 17.8 |
| T4 | P4-恩賞 | Imperial Grant | 28.9 | 22.6 (-6.4, 29.0) | 17.8 |
| T5 | P5-保舉 | Recommendation | 35.1 | -8.2 (-6.9, -1.2) | 17.8 |
| T6 | P6-詞科 | Graduate of Grace Palace Examination | 33.5 | 31.2 (8.3, 22.9) | 17.9 |
| T3 | P7-筆帖式 | Banner clerk | 37.6 | 40.5 (17.3, 23.2) | 18.2 |
| T2 | P8-天文生 | Student of Astronomy | 37.1 | -22.2 (-13.0, -9.2) | 17.6 |
| T1 | P9-醫士 | Student of Medicine | 29.8 | -18.2 (-13.0, -9.2) | 17 |
| D4 | P10-生員 | Licentiate | 36.4 | 10.5 (2.4, 8.1) | 17.8 |
| D6 | P11-監生 | Imperial Academy Collegian | 36.1 | 3.4 (-0.7, 4.1) | 17.8 |
| D5 | P12-官學生 | Student of the Banner School | 38.1 | 36.9 (16.5, 20.4) | 18.1 |
| D3 | P13-供事 | Senior Clerk | 39.1 | -27.2 (-4.5, -22.7) | 17.6 |
| D2 | P14-吏員 | Clerk | 39.9 | -31.8 (-4.7, -27.1) | 17.6 |
| D1 | P15-童生 | Student | 38 | -11 (-2.3, -8.7) | 17.7 |
| 4444 | P16-衍聖公 | Sacred Prince (Descendent of Confucius) | 31 | 386.7 (-5.0, 391.7) | 17.9 |
| 6666 | P17-一等輕車都尉 | First Commander of the Light Chariot Force | 15.4 | 184.2 (-13.3, 197.6) | 18.1 |
| 5555 | P18-二等輕車都尉 | Second Commander of the Light Chariot Force | 19.4 | 186.5 (-5.6, 192.1) | 18 |
| 3333 | P19-三等輕車都尉 | Third Commander of the Light Chariot Force | 24.5 | 172.7 (-6.7, 179.4) | 18.1 |
| 2222 | P20-騎都尉 | Senior Commander of the Cavalry | 28.8 | 157.3 (3.2, 154.2) | 18 |
| 1111 | P21-雲騎尉 | Junior Commander of the Cavalry | 29.5 | 144.3 (-4.2, 148.5) | 18.9 |
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Table [6](#table-441-*) also contains a column showing average effective money. This value is calculated by adding up all the money that a player receives in a given playthrough, both from the pool and from other players, and subtracting everything he has to pay, again both to the pool and directly to other players. Looking at the data in the table, it becomes immediately clear that for most *chushen* the game is – on average – pretty close to a zero-sum game, i.e. getting one provenance over the other in the beginning does not mean that the player should expect to win or lose more or less money compared to other *chushen*. Given the zero-sum nature of the game, this is of course not entirely unexpected, since all income must be balanced out with the expenses of the other players. It is nevertheless interesting to observe that at least at the level of *chushen*, the players are mostly not destined for a path from the start that will lead to them gaining or losing a lot of money with high probability.  The clearest exceptions to this are to be found in the hereditary ranks (P17-P21) which on average receive much more money from other players than they have to pay themselves. This is easily explained by the fact that they already receive a significant payout in the beginning just for the fact that they got this particular starting position. Because these provenances are so unlikely to occur compared to the regular *chushen*, they do not have a large effect on the overall expectation values of the other starting positions, i.e. in an average game, a player need not be afraid to have to pay out a lot of money to a fellow player who obtained a hereditary rank. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Among the other positions, the only chushen that on average have a significant positive return both in winning money from the pool as well as from other players are the two Manchu positions (P7, P12) and P6 (Special palace examination, *cike* 詞科). P1 (Honorary Licentiate, *yinsheng* 蔭生) and P4 (Imperial grace, *enshang* 恩賞) both have a negative expected return from the pool, but this is more than made up for by the significant amount of money they receive from other players.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"lhlur": [{"id": "14298532/5PCAUVA8", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
On the other end of the spectrum, the positions that on average lose more than a trivial amount of money are those that we categorized as incipient professionalism, i.e. the clerks (P13, P14) and Students of Astronomy and Medicine (P8, P9). This seems to point to a value system that did not cherish specialized knowledge (On the clerks see: <cite id="lhlur"><a href="#zotero%7C14298532%2F5PCAUVA8">(Kaske, 2012)</a></cite>). The latter two also had short paths and largely cul-de-sac careers within the same department (especially P9). Thus, our simulation confirms the intuition of the rule writer that suggests that players that receive one of these two chushen should bail out (see section [4.2](#subsection-4.2)).

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Finally, looking at the average final rank that players starting from the different chushen achieve, also shown in Table [6](#table-441-*), we can see that there does not seem to be a large difference. The average rank transformed to our linear scale over all playthroughs is slightly above 17.5, corresponding to a rank in the traditional system of between 2a and 1b. Aside from the lucky positions, two noticeable bumps are again the two Manchu chushen (P7, P12). This is presumably due to their privileged access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) which is pivotal to reach P352 and thereby the highest rank-class 1a. For Non-Manchus, this privilege is only granted to those top-tier jinshi degree holders who went through the Hanlin Academy (C56  *Hanlinyuan* 翰林院). Players from other backgrounds are forced into early retirement when they would have reached this position, thus cutting short their chance to reach a higher final rank. To spend some time at the highest rank is advantageous also in monetary terms, because instead of a progression in rank-class, the player becomes eligible for honorific rewards including palace titles (C60 *gongxian* 宮銜) and special awards (C64 *te’en* 特恩) which come with monetary gifts. Thus, this rule also explains the favorable status of the Manchu chushen in monetary terms noted above.

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-442-*"] -->
Did go through examination system?|Average number of hops until retirement|Average effective money (From/to pool, From/to other players)|Average final rank (1a = 19, unclassed = 1)|
-|-|-|-
Yes|36.8|5.9 (1.4, 4.5)|17.8|
No|37.3|-4.1 (-0.9, -3.1)|17.8|


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Aside from starting positions, we can also group the data by other properties that distinguish particular backgrounds. For example, Table [7](#table-442-*) shows the average outcomes for players who did or did not go through the examination system. For this purpose, we record during the simulation in a variable for each player whether they have visited one of the positions marked  as “exam” in our database, which are spread over several departments located adjacent to the *chushen* positions (C3, C4, C6, C7, C8). As can be seen, the most significant difference in outcomes between the players who visited one of these positions and those that did not is not in the number of moves or the achieved rank class, but in the monetary results of the game. Players who went through the examination system have a slightly positive expected return, originating mostly from payments the other players have to directly make to them.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Overall, our findings reveal that for all *chushen* positions, except the student of medicine (P9), the opportunities to get to the highest ranks are evenly spread. However, in terms of monetary reward, hereditary privilege and imperial grace trump all other provenances. Graduates of the imperial examinations also have positive returns on average, but much humbler than the hereditary group. This, again, may have been due to access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) which is pivotal to reach P352. If this is true, then only those examination candidates would benefit who reach the top-tier *jinshi* degree and were admitted to the Hanlin Academy (C56). Other provenances have slightly negative outcomes on average.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["section-45"] -->
### When would purchase be lucrative? 
<!-- #endregion -->

In the preceding section, we have analysed the role of provenance without purchase, i.e. in a setting where the players are completely subject to the roll of dice. As we have seen, a few hard to reach, yet especially favourable *chushen* can lead to high expected outcome, contrasted with middling results for most players. In this section, we will consider the game with the additional possibility of purchase. Since this poses some technical difficulties, we will start by describing the modifications to the simulation that were necessary to make this possible.


<!-- #region editable=true slideshow={"slide_type": ""} -->
In general, the question under which circumstances office purchase is beneficial to the player would require an extremely involved game theoretic analysis, because the strategies pursued by other players might affect the choice of whether one should buy an office or not. However, our purpose here is not to obtain an optimal strategy for playing the game. Rather, we are interested in understanding the reality of the game in a way that aligns with what the game designers and players could reasonably know about its mathematical realities. Since the next move after purchase will be determined through dice rolls and after that, potentially also the decisions of the others,  players are faced with a high amount of uncertainty. Furthermore, due to the abundance of positions that can be attained after leaving the *chushen*, the same configurations of player tokens being in certain positions would hardly ever be achieved again in subsequent playthroughs, meaning that past experience is of limited use in subsequent playthroughs.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"bz5lo": [{"id": "14298532/G5GNLPXX", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Hence, for the purposes of this study, we decided to implement a relatively simple artificial intelligence approach, that makes the decision of whether a position should be bought or not based on simulating a fixed number of playthroughs for each possible choice, giving a rough version of Monte Carlo Tree Search (For a similar application to a board game, see e.g. <cite id="bz5lo"><a href="#zotero%7C14298532%2FG5GNLPXX">(Szita et al., 2010)</a></cite>). Whenever a player has the choice to either purchase from the C14 list of “expectant officials by purchase”, or if necessary given their *chushen*, the position Imperial Academy Collegian (P11, see section [4.2](#subsection-42) above) or else throw the dice, all possible options, including not purchasing office, are evaluated by copying the game state, enacting the option under consideration and then continuing the game until it reaches its end. We will play 10 times for each of the options that could be purchased, and again 10 times for the option without purchase. After finishing these playthroughs, we then select the choice that resulted in the highest average monetary gains for the player for whom the algorithm is invoked. In case the player has purchased one of the auxiliary officials positions (P89 and P90) in their previous turn, and has to decide on one real position to move to in their current term, the same decision procedure is invoked to decide between the options.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
 Since our interpretation of the rules allows the players to purchase office from most positions, the other players might decide to purchase office in response to the different choices one player makes. For example, it might turn out to be beneficial to purchase office for a player *b* after player *a* has done so, in order to avoid falling behind the other players. However, considerations for potential reactions from *b* will have an impact on *a*’s decision to purchase in the first place. For example, if a purchase simply results in a stalemate because the other players can just counter it by purchasing themselves, it might not be beneficial for *a*  to purchase in the first place. In order to account for such phenomena, when executing the simulation of the purchase options described above, different choices are also simulated in a recursive manner for the other players. However, in order to stay true to the objective of not aiming towards an optimal strategy, but rather to reflect the uncertainty faced by the historic actors who participated in the game, we decided to limit the number of branches that are investigated in this way. In particular, in any simulated playthrough, at most four levels of recursive purchase decisions are evaluated, beyond which the game is simply played without purchase until the end. Furthermore, while for the initial simulation, each purchase option is evaluated ten times and the one giving the highest average chosen, for the nested simulations, each option is only evaluated once, and for those occurring in the third or fourth level of recursion, only a randomly chosen subset of options is evaluated at all.

<!-- #endregion -->

Even given these simplifications, the decision strategy outlined above requires considerable computational power, making each playthrough take significantly more time than was the case for the simulation without purchase. Hence, the simulation with purchase was only run for 2000 playthroughs, each with four players, giving 8000 playthroughs of individual players, during which 34,781 purchase decisions were evaluated. 


<!-- #region editable=true slideshow={"slide_type": ""} -->
As a first result,  the algorithm outlined above leads to  almost all the players purchasing office very early. In fact, in 7992 of the 8000 playthroughs of individual players, a purchase was made, on average occurring after throwing the dice 2.6 times (sd: 3.75). The decision to make a purchase instead of simply relying on dice rolls is supported quite strongly by the simulations, indicated by a high average difference between the simulated outcomes of the best purchase option and non-purchase. The average difference in monetary outcome of the ten simulations for the purchase option with the highest average outcome on the one hand, and the ten simulations for the option not to purchase on the other hand was 44.7 (sd: 32.2). However, when examining the results of the simulations closely, it becomes clear that in any case, the decision must be made under a considerable degree of uncertainty. The standard deviation of the results of the ten simulations for each option, averaged over all choices, is as high as 86.3. Given that after the purchase, the game mostly progresses by further dice throws, and potential actions by the other players which are also hard to predict, this is of course not surprising. Hence, even when including the potential of purchase, the experience of the historic players must still have been one dominated by luck and not planned decision making.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
One potential implication of allowing purchase in the rules of the game is that it might level the playing field, by giving players with an unfavorable *chushen* the chance to make up for their disadvantage. This is suggested by the rules themselves which strongly encourage Students of Astronomy and Medicine to bail out from their *chushen*. Table [8](#table-451-*), which displays the average outcomes of players by *chushen* with purchase shows that this is indeed the case. Firstly, purchase significantly reduces the number of hops until retirement for all players. Secondly, it reduces both losses and gains for most players, thus leveling the final results. There are exceptions. In comparison to Table [5](table-441-*), showing the situation without the purchase, the average results of which are also reproduced in Table [8](#table-451-*), some positions may turn their (average) fate from negative to positive (P5, P15) or from positive to negative (P11, P12). Observe that due to the lower number of total playthroughs, the hereditary positions are not included in Table [8](#table-451-*), since they were not visited enough times to obtain reliable results. Due to their immediate gain of a significant amount of money, we expect that they would retain an advantage above other positions.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
However, according to our interpretation of the rules, the more favorable *chushen* still have a head-start by not having to purchase the Imperial Academy Collegian (P11) first, limiting the equalizing effects of purchase. P8-10 and P13-15, who share this obligation, continue to be at a financial disadvantage. Most prominently, in comparison to the simulation without purchase, the monetary results of the adopted simulation favor Manchu *chushen* (P7, P12) even more strongly than before. We can speculate that this is because the Manchu-exclusive positions feature only in late-game. As we have explained in section [4.4](#section-44), privileged access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) in the late game is one of the key advantages of a Manchu *chushen*. Since the simulation with purchase leads to the early game progressing much faster than was the case without purchase, a late game advantage naturally becomes even more beneficial.

<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["LABEL TO ADD"]}} slideshow={"slide_type": ""} tags=["table-451-*"] -->
Dice|Position|Translation|Average number of hops until retirement (without purchase)|Average effective money (without purchase) |Average final rank (1a = 19, unclassed = 1) (without purchase)|
-|-|-|-|-|-
3456|P1-蔭生|Honorary Licentiate|25.3 (31.2)|7.0 (19.6) |18.1 (17.9)|
1144|P2-軍功|Military Merit|25.4 (35.8)|-41.8 (-11.1) |17.9 (17.7)|
DxDx|P3-貢生|Senior Licentiate, Tribute Student|25.5 (36.4)|0.0 (7.5) |18.0 (17.8)|
T4|P4-恩賞|Imperial Grant|27.4 (28.9)|28.7 (22.6)|17.7 (17.8)|
T5|P5-保舉|Recommendation|24.7 (35.1)|6.6 (-8.2)|17.9 (17.8)|
T6|P6-詞科|Graduate of Grace Palace Examination|26.5 (33.5)|-3.8 (31.2)|18.2 (17.9)|
T3|P7-筆帖式|Banner clerk|26.7 (37.6)|43.3 (40.5)|17.8 (18.2)|
T2|P8-天文生|Student of Astronomy|26.8 (37.1)|-8.5 (-22.2)|17.8 (17.6)|
T1|P9-醫士|Student of Medicine|26.3 (29.8)|-8.5 (-18.2)|17.8 (17.0)|
D4|P10-生員|Licentiate|25.4 (36.4)|-3.6 (10.5)|17.8 (17.8)|
D6|P11-監生|Imperial Academy Collegian|25.3 (36.1)|25.3 (3.4)|17.9 (17.8)|
D5|P12-官學生|Student of the Banner School|27.8 (38.1)|27.8 (36.9) |18.1 (18.1)|
D3|P13-供事|Senior Clerk|26.4 (39.1)|-3.5 (-27.2) |17.9 (17.6)|
D2|P14-吏員|Clerk|26.4 (39.9)|-2.8 (-31.8) |17.9 (17.6)|
D1 |P15-童生|Student|25.6 (38)|0.6 (-11)|17.9 (17.7)
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In summary, our numerical findings do confirm a tendency to speed up promotion and level the results between the different *chushen*, creating a strong incentive to purchase, especially (but not only) for players seeking to escape from an unfavourable start in the game. As soon as one player starts to purchase, other players will follow. The findings from our simulation show that in almost all games purchases were made. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
This confirms the intuition of some modern day editions of the game that discourage the use of this mechanism, because it makes the game unbalanced and, presumably, less fun.  However, as we have seen, considerable uncertainty remains even with purchase. Even if,  for certain *chushen* provenances, results are more or less favorable with purchase on average, this is far from guaranteed for the individual player.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Conclusions
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The goal of this paper has been twofold: First, we wanted to understand what kind of bureaucratic reality the game mimics and how close it came to this reality. We also hoped to learn how the game designer understood and judged this reality. Secondly, we wanted to know how the category of *chushen* provenances, namely the initial status of entrants into the enfranchised holders of official rank (hereditary privilege, Imperial grace, examination, incipient professionalism), influenced game chances.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In order to answer these questions, we have used two digital approaches. First, we have modelled the game as a network, and applied techniques inspired from research into transportation networks to understand the flow of personnel between the positions on the game board. Second, we have used a simulation to obtain accurate numerical values for the expected outcomes of the game both with and without the possibility of purchase. Our implementation shows the feasibility of applying digital methods to a historic board game. As we have seen, this proved to be particularly challenging because the rules of the game contain many intricate provisions to increase its realism.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
We found that the game was both a mimicry and metaphor of real-world nineteenth-century Qing officialdom.  As a didactic game, *Mandarin Promotions* mimicked the statutory regulations of rank promotions as closely as possible on a single chart, considering the necessary symmetry in the dice moves (mostly limited to six options). At the same time, the general outlook of its anonymous designer was an optimistic one, different from the original intentions of the Magie’s *Landlord Game* or the Böttger’s *Bürocratopoly* which started out as social criticism. Purchase of rank is included in this optimism as a viable and, in lived reality, completely legal option. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
At the same time, our simulation of the experiences made by different *chushen* provenances show that, far from the meritocratic mandarinate imagined by China-watchers and historians since the European enlightenment, the life chances depicted in the game were skewed towards hereditary privilege (especially the Manchus) and imperial grace. When including the choice of office purchase, this created strong incentives to seek promotion by that venue leading to pervasive venality. As the poem cited in section [1](#section-1) said: “Good offices in fact are all up for pay.” Uncertainty and luck, on the other hand, pervaded the choices for  both paths, the presumably meritocratic “regular” path and the venal “irregular” path into officialdom. Considering the popularity of the game throughout the nineteenth century, we are inclined to see this as an expression of the shared life experiences of the players, many of whom were aspiring official status themselves. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["bibliography"] -->
<!-- BIBLIOGRAPHY START -->
<div class="csl-bib-body">
  <div class="csl-entry"><i id="zotero|14298532/T4BB86FW"></i>Bell, D. A. (2015). <i>The China Model: Political Meritocracy and the Limits of Democracy</i>. Princeton University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/WB58FURK"></i>Blondel, V. D., Guillaume, J.-L., Lambiotte, R., &#38; Lefebvre, E. (2008). Fast unfolding of communities in large networks. <i>Journal of Statistical Mechanics: Theory and Experiment</i>, <i>2008</i>(10), 1–12. <a href="https://doi.org/10.1088/1742-5468/2008/10/P10008">https://doi.org/10.1088/1742-5468/2008/10/P10008</a></div>
  <div class="csl-entry"><i id="zotero|14298532/Q5VDL4VL"></i>Bourdieu, P. (1990). Book I: Critique of Theoretical Reason. In <i>The Logic of Practice</i> (pp. 22–141). Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/T54NP4X3"></i>Brunnert, H. S. (Hippolit S., &#38; Hagelstrom, V. V. (1912). <i>Present day political organization of China</i>. Book World. <a href="http://archive.org/details/presentdaypoliti00brunuoft">http://archive.org/details/presentdaypoliti00brunuoft</a></div>
  <div class="csl-entry"><i id="zotero|14298532/G53Z38BI"></i>Caillois, R. (2001). <i>Man, Play, and Games</i>. University of Illinois Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/6A3DYQPG"></i>Chen, B. (2019). <i>Origins and Career Patterns of the Qing Government Officials (1850-1912): Evidence from the China Government Employee Dataset-Qing (CGED-Q)</i> [Ph.D. dissertation]. Hong Kong University of Science and Technology.</div>
  <div class="csl-entry"><i id="zotero|14298532/BMQLXB3T"></i>Chen, B., Campbell, C., Ren, Y., &#38; Lee, J. (2020). Big Data for the Study of Qing Officialdom: The China Government Employee Database-Qing (CGED-Q). <i>Journal of Chinese History</i>, <i>4</i>(2), 431–460. <a href="https://doi.org/10.1017/jch.2020.15">https://doi.org/10.1017/jch.2020.15</a></div>
  <div class="csl-entry"><i id="zotero|14298532/2XBUU6KC"></i>Chu, S. (2022). The longer abolition of the Chinese imperial examination system (1900s–1910s). <i>International Journal of Asian Studies</i>, <i>20</i>(2), 721–737.</div>
  <div class="csl-entry"><i id="zotero|14298532/GE6RH8S7"></i>Culin, S. (1895). <i>Chinese Games with Dice and Dominoes</i>. U.S. Government Printing Office.</div>
  <div class="csl-entry"><i id="zotero|14298532/AJMN2YBW"></i>DDR-Museum. (n.d.). <i>Die Geschichte Des Spiels Und Seines Erfinders Martin Böttger, Bürokratopoly</i>. <a href="https://www.buerokratopoly.de/portfolio/geschichte-des-spiel/">https://www.buerokratopoly.de/portfolio/geschichte-des-spiel/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/YCJWD8HN"></i>Duindam, J. (2015). <i>Dynasties: A Global History of Power, 1300–1800</i>. Cambridge University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/EN5WKUSS"></i>Elman, B. A. (2000). <i>A cultural history of civil examinations in late imperial China</i>. Univ of California Press. <a href="https://books.google.com/books?hl=de&#38;lr=&#38;id=qkslDQAAQBAJ&#38;oi=fnd&#38;pg=PR11&#38;ots=efFTfBM4do&#38;sig=4yS98YaaPqAu5tohX4oesoAO0SM">https://books.google.com/books?hl=de&#38;lr=&#38;id=qkslDQAAQBAJ&#38;oi=fnd&#38;pg=PR11&#38;ots=efFTfBM4do&#38;sig=4yS98YaaPqAu5tohX4oesoAO0SM</a></div>
  <div class="csl-entry"><i id="zotero|14298532/SQFMMJP7"></i>Elman, B. A. (2013). <i>Civil Examinations and Meritocracy in Late Imperial China</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/387PSRU9"></i>Graeber, D. (2015). <i>The Utopia of Rules: On Technology, Stupidity, and the Secret Joys of Bureaucracy</i>. Melville House.</div>
  <div class="csl-entry"><i id="zotero|14298532/6RRN59QA"></i>Groote, J. F., Wiedijk, F., &#38; Zantema, H. (n.d.). A Probabilistic Analysis of the Game of the Goose. <i>SIAM Review</i>, <i>58</i>(1), 143–155.</div>
  <div class="csl-entry"><i id="zotero|14298532/7QCP8KGW"></i>Guy R. K. (2014). Routine Promotions: Li Hu and the Dusty Byways of Empire. In Duindam J. &#38; Dabringhaus S. (Eds.), <i>The Dynastic Centre and the Provinces: Agents and Interactions</i> (pp. 74–93). Brill. <a href="https://opendata.uni-halle.de//handle/1981185920/110615">https://opendata.uni-halle.de//handle/1981185920/110615</a></div>
  <div class="csl-entry"><i id="zotero|14298532/XRLLY3EK"></i>Helliwel, D. (2014, January 10). The Promotion Chart. <i>SERICA</i>. <a href="https://serica.blog/2014/01/10/the-promotion-chart/">https://serica.blog/2014/01/10/the-promotion-chart/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/VXYXAJIC"></i>Ho, P. (1980). <i>The Ladder of Success in Imperial China: Aspects of Social Mobility, 1368-1911</i>. Columbia University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/B4NHBRJH"></i>Hu, H. 胡恒. (2013). Tingzhi qiyuan jiqi zai Qingdai de yanbian 厅制起源及其在清代的演变. <i>Wen Shi 文史</i>, <i>2</i>, 253–287.</div>
  <div class="csl-entry"><i id="zotero|14298532/3TJV8LU6"></i>Hu, H. 胡恒, Chen, B. 陳必佳, &#38; Kang, W. 康文林. (2020). Qingdai zhifu xuanren de kongjian yu lianghua fenxi: zi zhengqu fendeng, Jinshenlu shujuku wei zhongxin 清代知府選任的空間與量化分析－以政區分等、《縉紳錄》數據庫為中心. <i>Xinya Xuebao 新亞學報</i>, <i>37</i>, 339–398.</div>
  <div class="csl-entry"><i id="zotero|14298532/CTD5EWCD"></i>Hucker, C. O. (1985). <i>A Dictionary of Official Titles in Imperial China</i>. Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/DVDEVB62"></i>Huizinga, J. H. (1950). <i>Homo Ludens: A Study of the Play-element in Culture</i>. Beacon Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/5PCAUVA8"></i>Kaske, E. (2012). Metropolitan Clerks and Venality in Qing China: The Great 1830 Forgery Case. <i>T’oung Pao</i>, <i>98</i>(1–3), 217–269. <a href="https://doi.org/10.1163/156853212X634626">https://doi.org/10.1163/156853212X634626</a></div>
  <div class="csl-entry"><i id="zotero|14298532/BK2CS6TS"></i>Kaske, E. (2018). Austerity in times of war: government finance in early nineteenth-century China. <i>Financial History Review</i>, <i>25</i>(1), 71–96. <a href="https://doi.org/10.1017/S0968565017000300">https://doi.org/10.1017/S0968565017000300</a></div>
  <div class="csl-entry"><i id="zotero|14298532/LADB2N7R"></i>Kaske, E. (2024). Power for a Price: The Purchase of Official Appointments in Qing China by Lawrence Zhang (review). <i>Harvard Journal of Asiatic Studies</i>, <i>84</i>(1–2), 236–241. <a href="https://muse.jhu.edu/pub/109/article/948875">https://muse.jhu.edu/pub/109/article/948875</a></div>
  <div class="csl-entry"><i id="zotero|14298532/9GEGGN5R"></i>Keliher, M. (2016). Administrative Law and the Making of the First Da Qing Huidian. <i>Late Imperial China</i>, <i>37</i>(1), 55–107. <a href="https://doi.org/10.1353/late.2016.0007">https://doi.org/10.1353/late.2016.0007</a></div>
  <div class="csl-entry"><i id="zotero|14298532/WSGVR2JV"></i>Kondō, H. 近藤秀樹. (1963a). Shindai no ennō to kanryō shakai no shūmatsu (1) 清代の捐納と官僚社会の終末-上-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(2), 82–110. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877019">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877019</a></div>
  <div class="csl-entry"><i id="zotero|14298532/S78TH7KN"></i>Kondō, H. 近藤秀樹. (1963b). Shindai no ennō to kanryō shakai no shūmatsu (2) 清代の捐納と官僚社会の終末-下-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(4), 60–85. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877036">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877036</a></div>
  <div class="csl-entry"><i id="zotero|14298532/DGARYT8Z"></i>Kondō, H. 近藤秀樹. (1963c). Shindai no ennō to kanryō shakai no shūmatsu (3) 清代の捐納と官僚社会の終末-中-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(3), 77–100. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877028">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877028</a></div>
  <div class="csl-entry"><i id="zotero|14298532/IVZDEUYV"></i>Libu. (1969). <i>Qinding libu zeli 钦定吏部则例 [Regulations of the Ministry of Personnel]</i> (Facsimile of the 1843 edition). Chengwen chubanshe 成文出版社.</div>
  <div class="csl-entry"><i id="zotero|14298532/3TYGCHP7"></i>Lo, A. (2004). Official Aspirations: Chinese Promotion Games. In C. Mackenzie &#38; I. Finkel (Eds.), <i>Asian Games: The Art of Contest</i> (pp. 64–75). Asia Society (USA). <a href="https://eprints.soas.ac.uk/1294/">https://eprints.soas.ac.uk/1294/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/T57KB3SN"></i>Marsh, R. M. (1962). The Venality of Provincial Office in China and in Comparative Perspective. <i>Comparative Studies in Society and History</i>, <i>4</i>(4), 454–466. JSTOR. <a href="https://www.jstor.org/stable/177694">https://www.jstor.org/stable/177694</a></div>
  <div class="csl-entry"><i id="zotero|14298532/9PCJFR3C"></i>Metzger, T. A. (1983). <i>The Internal Organization of Ch’ing Bureaucracy: Legal, Normative, and Communication Aspects</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/J8BBF2K4"></i>Meyer-Fong, T. (2013). <i>What Remains: Coming to Terms with Civil War in 19th Century China</i>. Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/VC6E2BGP"></i>Morgan, C. (2004). The Chinese Game of Shengguan tu. <i>Journal of the American Oriental Society</i>, <i>124</i>(3), 517–532. JSTOR. <a href="https://doi.org/10.2307/4132278">https://doi.org/10.2307/4132278</a></div>
  <div class="csl-entry"><i id="zotero|14298532/LC5FSDKM"></i>Needham, M., &#38; Hodler, A. E. (2019). <i>Graph Algorithms: Practical Examples in Apache Spark and Neo4j</i>. O’Reilly Media, Inc.</div>
  <div class="csl-entry"><i id="zotero|14298532/X6LTB4FQ"></i>Ngai, M.-Y. M. (2010). <i>From Entertainment to Enlightenment: A Study on a Cross-Cultural Religious Board Game with Emphasis on the Table of Buddha Selection Designed by Ouyi Zhixu of the Late Ming Dynasty</i> [Ph.D. dissertation]. University of British Columbia.</div>
  <div class="csl-entry"><i id="zotero|14298532/ZH6Y34YM"></i>Pan, G. 潘國森. (2017). <i>Panshi chongding Qingdai Shengguantu 潘氏重訂清代陞官圖</i>. Showwe Books for Sunyata 新一堂&#38;秀威書店.</div>
  <div class="csl-entry"><i id="zotero|14298532/DJQAH7XE"></i>Pao Chao Hsieh. (1925). <i>The Government of China (1644-1911)</i>. Johns Hopkins University.</div>
  <div class="csl-entry"><i id="zotero|14298532/RIQ5GUEC"></i>Peng, P. (2022). <i>Pen and Sword: Meritocracy, Conflicts, and Bureaucratic Appointments in Imperial China</i> [Ph.D. dissertation]. Duke University.</div>
  <div class="csl-entry"><i id="zotero|14298532/S5JC8IGD"></i>Pilon, M. (2015). <i>The Monopolists: Obsession, Fury, and the Scandal Behind the World’s Favorite Board Game</i>. Bloomsbury Publishing USA.</div>
  <div class="csl-entry"><i id="zotero|14298532/JDFA84RJ"></i>Porter, D. C. (2023). <i>Slaves of the Emperor: Service, Privilege, and Status in the Qing Eight Banners</i>. Columbia University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/V9HJ834C"></i>Puk, W. K. 卜永堅. (2010). <i>Youxi guanchang: Shengguantu yu Zhongguo guanzhi wenhua 遊戲官場: 升官圖與中國官制文化</i>. Zhonghua Shuju 中華書局.</div>
  <div class="csl-entry"><i id="zotero|14298532/YEVRUWRU"></i>Schmidt-Madsen, J. (2019). <i>The Game of Knowledge: Playing at Spiritual Liberation in 18th-and 19th-Century Western India</i> [Ph.D. dissertation]. University of Copenhagen.</div>
  <div class="csl-entry"><i id="zotero|14298532/DEYG8UIS"></i>Stover, L. E. (1974). <i>The Cultural Ecology of Chinese Civilization: Peasants and Elites in the Last of the Agrarian States</i>. Pica Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/8EQW4XQE"></i>Sung, P.-J. 宋秉仁. (2005). Shengguantu youxi yange kao 陞官圖遊戲沿革考. <i>Taiwan Shi Da Lishi Xuebao 臺灣師大歷史學報</i>, <i>33</i>, 27–78. <a href="https://www.airitilibrary.com/Publication/alDetailedMesh?docid=03019667-200506-x-33-27-78-a">https://www.airitilibrary.com/Publication/alDetailedMesh?docid=03019667-200506-x-33-27-78-a</a></div>
  <div class="csl-entry"><i id="zotero|14298532/G5GNLPXX"></i>Szita, I., Chaslot, G., &#38; Spronck, P. (2010). Monte-Carlo Tree Search in Settlers of Catan. In H. J. van den Herik &#38; P. Spronck (Eds.), <i>Advances in Computer Games</i> (pp. 21–32). Springer. <a href="https://doi.org/10.1007/978-3-642-12993-3_3">https://doi.org/10.1007/978-3-642-12993-3_3</a></div>
  <div class="csl-entry"><i id="zotero|14298532/WJGDPPDF"></i>Tatz, M., &#38; Kent, J. (1977). <i>Rebirth: The Tibetan Game of Liberation</i>. Anchor Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/PX4XEZRW"></i>Wang, K. 王闓運. (1983). <i>Xiangjun zhi 湘軍志 [History of the Hunan Army]</i>. Yue Lu shushe.</div>
  <div class="csl-entry"><i id="zotero|14298532/MGTNKIZA"></i>Wilkinson, E. (2012). <i>Chinese History: A New Manual</i>. Harvard Asia Center.</div>
  <div class="csl-entry"><i id="zotero|14298532/MNBH9DQS"></i>Will, P.-É. (2020). <i>Handbooks and Anthologies for Officials in Imperial China: A Descriptive and Critical Bibliography</i>. Brill.</div>
  <div class="csl-entry"><i id="zotero|14298532/XZSI5NY6"></i>Wu, S. 吴思. (2009). <i>Qian Guize: Zhongguo Lishi Zhong De Zhenshi Youxi 潜规则 : 中国历史中的真实游戏</i> (Di 1 ban). Fudan da xue chu ban she.</div>
  <div class="csl-entry"><i id="zotero|14298532/9XED7GPL"></i>Wu, Y. 伍跃. (2021). <i>Zhongguo de juanna zhidu yu shehui 中国的捐纳制度与社会</i>. 江苏人民出版社. <a href="https://book.douban.com/subject/24734224/">https://book.douban.com/subject/24734224/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/SYYWS26A"></i>Wu, Y. 伍躍. (2022). Jinshenlu yu Qingdai difang guanyuan renshi zhidu yanjiu 縉紳錄與清代地方官員人事制度研究. <i>Xinya Xuebao 新亞學報</i>, <i>39</i>, 1–62.</div>
  <div class="csl-entry"><i id="zotero|14298532/F8METVWQ"></i>Xu, B. (2021). <i>Chairman Mao’s Children: Generation and the Politics of Memory in China</i>. Cambridge University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/9YAWZZJ4"></i>Zhang, L. (2023). <i>Power for a Price: The Purchase of Official Appointments in Qing China</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/I2NEPQBN"></i>Zhang, M. 章名未. (2023). Tang Song caixuange yu guanzhi zhishi de chuanbo: yi Liu Ban “Hanguanyi Caixuan” weili 唐宋彩選格與官制知識的傳播：以劉攽《漢官儀彩選》為例. <i>Tang Yanjiu 唐研究</i>, <i>24</i>, 251–271.</div>
  <div class="csl-entry"><i id="zotero|14298532/SDB4J2CY"></i>桂笙 Guisheng. (1887, March 1). Ti Shengguanlu, qing Guisheng xiansheng yintan zhengkan  題陞官圖錄，請桂笙先生吟壇正刊. <i>Shenbao  申報</i>.</div>
</div>
<!-- BIBLIOGRAPHY END -->
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}

```
