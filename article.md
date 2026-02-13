---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} tags=["title"] -->
# Gaming the Qing Mandarinate: Digital Approaches to a Nineteenth-Century Chinese Board Game
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["contributor"] -->
 ### Elisabeth Kaske [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-7091-5885) 
 Universität Leipzig
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["contributor"] -->
### Florian Keßler [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0009-0002-6663-1385) 
Friedrich-Alexander-Universität Erlangen-Nürnberg
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["copyright"] -->
[![cc-by-nc-nd](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/) 
© Elisabeth Kaske - Florian Keßler. Published by De Gruyter in cooperation with the University of Luxembourg Centre for Contemporary and Digital History. This is an Open Access article distributed under the terms of the [Creative Commons Attribution License CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/)

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["keywords"] -->
Qing dynasty (1644-1911), Bureaucracy, Boardgame, Graph Database, Monte Carlo
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"59b7z": [{"id": "14298532/V8FFRKCS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["abstract"] -->
How did people in the Qing dynasty (1644–1911) imagine careers in the officialdom? This study explores the historical board game Mandarin Promotions (*Shengguantu* 陞官圖), a bureaucratic career race game played with dice that resembles Milton Bradley’s Checkered Game of Life, but mirrors the complex Qing personnel system in striking detail. Similar bureaucratic career games have been attested in China for centuries, one version from the late Ming Dynasty (early 17th century) for military and civil officials was already called "Mandarin Promotions". This paper investigates a popular nineteenth-century game table, for civil officials only, which added two major innovations: monetary gamble and the option to purchase office, i.e. to buy one's position in the bureaucratic order. This transformed bureaucratic advancement from a race driven by fateful dice into a more exciting playing field of chance, strategy, and social commentary.

Using a late nineteenth-century version reproduced by Puk Wing Kin (<cite id="59b7z"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>), we modeled the game’s 434 positions across 66 departments as a network of career paths leading to 18 final ranks. Comparing this structure with official promotion charts from Qing statutes (pre-1843), we found a strong correspondence, confirming the 1840 dating of the extant board and showing that the game reflected contemporary bureaucratic ideals rather than being pure invention. The game thus offers a rare insight into how the Qing world imagined officialdom—structured, rule-bound, but also open to luck, privilege, and purchase.

The second part of our paper employed Monte Carlo simulations to address two questions. First, how “meritocratic” were the imagined careers, considering that starting positions correspond to distinct entry routes into officialdom—hereditary privilege, the imperial examinations, military service, patronage, and what we call “incipient professionalism.” Our simulations show that hereditary privilege outperformed other routes, while exam success offered moderate mobility and all others lagged behind. Secondly, we ask when was office purchase a rational choice? Modeling strategic play revealed that, when allowed, most simulated players chose to buy rank early in the game. Office purchase slightly levelled the playing field in terms of speed, but did not undermine the benefits of hereditary privilege in terms of monetary gains. This might reflect contemporary anxieties that office purchase undermined merit while still failing to erase social hierarchies.

Ultimately, Mandarin Promotions transforms Qing bureaucratic ideals into a playable form, revealing how chance, money, and inherited status shaped both the imagination and critique of officialdom in late imperial China.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-1-*"] -->
## Introduction
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Our study explores the historical board game Mandarin Promotions (*Shengguantu* 陞官圖), a career game where players start from multiple starting positions to race up the ladder of Qing dynasty (1644-1911) bureaucratic ranks. As a career race played by dice, the game resembles Milton Bradley's famous nineteenth-century *Checkered Game of Life*. However, as it closely mirrored the statutory personnel system of the Qing bureaucracy, Mandarin Promotions was far more complex (simplified versions circulated as well, but they are not considered here). What does the board game then tell us about popular perceptions of the Qing mandarinate? 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"39f0v": [{"id": "14298532/LW63Q9KW", "source": "zotero"}], "7j15a": [{"id": "14298532/G7HQLMZ7", "source": "zotero"}], "8o45d": [{"id": "14298532/DN3VH8TV", "source": "zotero"}], "ja7bn": [{"id": "14298532/V8FFRKCS", "source": "zotero"}], "jtni7": [{"id": "14298532/5ZHJZ28C", "source": "zotero"}], "k5hww": [{"id": "14298532/BXSXXT84", "source": "zotero"}], "l9jgr": [{"id": "14298532/FT4X2A27", "source": "zotero"}], "xctms": [{"id": "14298532/PQVWKAP3", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Bureaucratic promotion games in China go back to the ninth century AD. By the Ming dynasty (1368-1644), playing such games had become a fixture in the New Year’s rituals (<cite id="39f0v"><a href="#zotero%7C14298532%2FLW63Q9KW">(Morgan, 2004)</a></cite>, <cite id="7j15a"><a href="#zotero%7C14298532%2FG7HQLMZ7">(Lo, 2004)</a></cite>, <cite id="l9jgr"><a href="#zotero%7C14298532%2FFT4X2A27">(Sung Ping-Jen 宋秉仁, 2005)</a></cite>, <cite id="jtni7"><a href="#zotero%7C14298532%2F5ZHJZ28C">(Ngai, 2010)</a></cite>). A game named “Mandarin Promotions,” which included civil and military officials and used six dice, goes back to the Ming dynasty and was first described in Europe in 1694 (<cite id="k5hww"><a href="#zotero%7C14298532%2FBXSXXT84">(Hyde, 1694)</a></cite>). However, in the nineteenth century a new version of the game, which was played with four dice and only included civil officials, eclipsed the older six-dice version. Mandarin Promotions game charts were ephemerals printed on paper, not wooden boards as we know from well-known board games like Chinese Chess or Go. The earliest surviving xylographed game chart of this new version is dated 1840 and held at the Oxford Bodleian library (<cite id="xctms"><a href="#zotero%7C14298532%2FPQVWKAP3">(Helliwel, 2014)</a></cite>). A lithography published in post-1870s Shanghai has been reproduced by Puk Win Kin with playable instructions (<cite id="ja7bn"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>). The two charts are closely related. Both carry almost the same game rules with few if telling additions and the same preface (with the date removed from the later versions). The four-dice civil-officialdom version became extremely popular and continued to circulate with only slight alterations, as the many surviving game charts attest (see for example: <cite id="8o45d"><a href="#zotero%7C14298532%2FDN3VH8TV">(Culin, 1895)</a></cite>, 504-507). Its popularity was probably due to two new features in the game rules not seen in earlier versions: the inclusion of monetary stakes and of the option to purchase office. This added the excitement of gambling and strategy into a game otherwise entirely driven by dice throws.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"qhwls": [{"id": "14298532/V8FFRKCS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Our study is based on the chart reproduced by Puk (<cite id="qhwls"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>). Players race from 22 starting positions through 434 positions distributed across 66 departments to reach 18 ranked final positions. Our exploration unfolds in two steps: First, we had to show whether the game board was a realistic reflection on the Qing bureaucracy or instead was pure fantasy. We hence needed to investigate if there was a correspondence between the game moves and the statutory promotion charts of the Qing bureaucracy, that is, the bureaucratic order as codified in sources like the “Collected Statutes” (*Huidian* 會典) and other official regulations, rather than the actual functioning of Qing officialdom. We also examined if and how the game designer has subtly introduced social commentary into his game chart.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"fohza": [{"id": "14298532/FVGZ3ZFN", "source": "zotero"}], "ndt4z": [{"id": "14298532/B4HFQQLN", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In a second step, we used Monte Carlo simulations to answer two main research questions: Firstly, different from comparable games in Asia and Europe, the starting point of *Mandarin Promotions* is outside the game chart. The first roll of dice decides from which of the 22 starting positions, including 15 positions designated as “*chushen* 出身” and 7 positions of hereditary nobility (*shixi* 世襲), the player will start his journey through the game, and several of the dice combinations employed are exclusive to this first roll. Chushen positions mimic the emic notion of “*chushen*” (literally “origin [of one’s public standing]”) which is most commonly understood as “credentials” represented by the degrees of the civil service examinations, but Chen Bijia in her study of the official directories found 837 different types of entries in the chushen field (<cite id="ndt4z"><a href="#zotero%7C14298532%2FB4HFQQLN">(Chen, 2019)</a></cite>, 48). Chu Shiuon has shown that *chushen* survived the abolition of those examinations in 1905 hinting at a broader meaning of the term (<cite id="fohza"><a href="#zotero%7C14298532%2FFVGZ3ZFN">(Chu Shiuon 徐兆安, 2023)</a></cite>). On post-1840 civil-official game charts, most examination degrees are not even included in the “*chushen*” category. Instead, there is a variety of *chushen*, which can be broadly categorized into hereditary privilege (including Manchu heritage), the imperial examinations, military merit, patronage, as well as what we call “incipient professionalism.” We may therefore perceive chushen more broadly as the dividing line between commoner status (and hence outsider to the game) and enfranchised holder of imperially sanctioned standing. Incidentally, the term “*juwai* 局外”, “outside the game,” in modern Chinese still literally denotes the “outsider,” *juwairen* 局外人, in general. However, this is a game, after all. Do these *chushen* grant an equal playing field? Or do some *chushen* have better opportunities than others to get ahead and win money in the game? How “meritocratic” was the imagined official career for the various starting positions? 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"3o9ek": [{"id": "14298532/PB9GMRPC", "source": "zotero"}], "3p3c3": [{"id": "14298532/IJAXKZ39", "source": "zotero"}], "5te3u": [{"id": "14298532/V8FFRKCS", "source": "zotero"}], "ehhjp": [{"id": "14298532/IJAXKZ39", "source": "zotero"}], "h3d8a": [{"id": "14298532/Q3B2LDZ3", "source": "zotero"}], "q2916": [{"id": "14298532/6XCI2QWJ", "source": "zotero"}], "qsi6n": [{"id": "14298532/CWESQSGQ", "source": "zotero"}], "s070j": [{"id": "14298532/DLXZH9IP", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Secondly, given that office purchase is the only aspect of the game that gives players the opportunity to actively influence their fate, we ask under which circumstances purchasing office would be a good strategy. Chinese historiography has long focused the civil service examinations and paid limited attention to alternative paths into officialdom, such as purchase or recommendation (<cite id="3o9ek"><a href="#zotero%7C14298532%2FPB9GMRPC">(Ho, 1980)</a></cite>, 104; <cite id="qsi6n"><a href="#zotero%7C14298532%2FCWESQSGQ">(Elman, 2000)</a></cite>, 126-127). New research has shown the pervasiveness of office purchase throughout the entire Qing dynasty (<cite id="3p3c3"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>), but one of the authors of this paper has argued that (legal) office selling by the state actually expanded since the early 1800s (<cite id="h3d8a"><a href="#zotero%7C14298532%2FQ3B2LDZ3">(Kaske, 2011)</a></cite>; <cite id="q2916"><a href="#zotero%7C14298532%2F6XCI2QWJ">(Kaske, 2012)</a></cite>; <cite id="s070j"><a href="#zotero%7C14298532%2FDLXZH9IP">(Kaske, 2018)</a></cite>). We hypothesize that the intrusion of purchase into the game reflected this expansion. As we will see, the few if telling changes in rules and added positions in later versions of the game are all related to the purchase of official rank. Puk Win Kin discourages the practice for modern players so as to maintain an equal playing field (<cite id="5te3u"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>, 28). However, how did historical players relate to office purchase, given that it was entirely legal and very common during their time (<cite id="ehhjp"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>)?
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The body of this paper has four main sections. In [Can we study a historical board game as historians?](#anchor-section-2-*), we will first explain why and how we apply a historical approach to the game. In brief, we argue, that comparing the official promotion charts with the game chart is a valid approach, because both serve as “utopias of rule” (in David Graeber’s term) that can well explain bureaucratic ideals or aspiration but not claim credence for realities on the ground.  [Playing Mandarin Promotions](#anchor-section-3-*) will present the game rules, our data model, and our digital methodologies. [“Utopias of Rules?”](#anchor-section-4-*) uses Neo4J and Gephi to model both the game and the bureaucratic promotion charts as networks of career paths that lead through pivotal positions to the highest rank-classes. We found that the moves on the game chart, to a large degree, corresponded with pre-1843 regulations. This confirmed the game’s original creation in 1840 and its expressed didactic intent. In addition, we studied how the game designer(s) creatively assigned quasi “meritocratic” names like “virtue”, “talent”, effort”, “mediocre”, “weak”, or “corrupt” to the numeric combinations of the dice movements to understand how Qing contemporaries perceived prestigious or less prestigious positions within the bureaucracy.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In [Equal opportunity?](anchor-section-5-*), the center piece of this study executed by Florian Keßler, we use a Monte Carlo simulation to explore how the game designers distributed winning chances for each of the 22 starting points. The outcomes show that *Mandarin Promotions* as a dice game maintains suspense by giving most *chushen* positions equal chances to move up the ladder of official ranks under great uncertainty. However, the actual monetary winning chances show the inequities of the system of promotions, giving advantages to hereditary privilege and Imperial grace and disadvantages to “incipient professionalism,” while examination graduates enjoy modest success. Secondly, given that office purchase is the only aspect of the game that gives players the opportunity to actively influence their fate, we ask under which circumstances purchasing office would be a good strategy. Given the complicated structure of the game, our Monte Carlo simulation required an implementation of the game rules in a program with considerable complexity. The results show that purchase actually works to slightly level the playing field, especially in terms of promotion speed. As a result, given the opportunity, players will overwhelmingly choose to engage in this possibility, mostly early in the game, confirming intuitions that office purchase ruins the suspense of the game. At the same time, however, uncertainty remains high even for purchasers, and office purchase also does not eliminate inherent inequities in the distribution of chances for monetary gain. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In conclusion, our playful engagement with the Qing mandarinate did yield new insights into how contemporaries imagined the world of career-making in a diverse yet monarchic society.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-2-*"] -->
## Can we study a historical board game as historians?
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"85u5c": [{"id": "14298532/G7HQLMZ7", "source": "zotero"}], "e20si": [{"id": "14298532/V8FFRKCS", "source": "zotero"}], "kypjk": [{"id": "14298532/DN3VH8TV", "source": "zotero"}], "lck2q": [{"id": "14298532/QPXW5GHH", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Mandarin Promotions was a board game most typically played during the Chinese New Year’s celebrations. During the Qing, the game was played by all walks of life, including literati and official families, who were normally coy to admit gambling within their ranks, by clerks, private secretaries and servants related to official life, as well as by commoners as distant to Qing officialdom as Chinese immigrants in California where Culin found the game in 1895 (<cite id="kypjk"><a href="#zotero%7C14298532%2FDN3VH8TV">(Culin, 1895)</a></cite>, 504-507). While officials certainly had better tools to understand their career options, the game’s didactic intent (discussed below) likely served broader populations to understand their bureaucratic reality. As a New Year’s ritual, moreover, the game lined up with similar auspicious promotion games like *Optimus Tally* (*Zhuangyuan Chou* 狀元籌) that gamified the civil examinations. These games transposed players into what Seligman has called an “as if” or “could be” world, a subjunctive universe “that makes our shared social world possible” (<cite id="lck2q"><a href="#zotero%7C14298532%2FQPXW5GHH">(Seligman et al., 2008)</a></cite> 7; <cite id="85u5c"><a href="#zotero%7C14298532%2FG7HQLMZ7">(Lo, 2004)</a></cite>, 72-73). Although largely obsolete now, Puk Win Kin still saw the game chart of *Mandarin Promotions* sold in stores for ritual goods in Hong Kong as late as 2011 (<cite id="e20si"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>, 4).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"eafmd": [{"id": "14298532/C92QNES9", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
During the New Year’s holiday of 1887, when the Qing mandarinate was still well alive, a group of literati entered this subjunctive universe to play a few rounds of *Mandarin Promotions* in Shanghai. One of them put his thoughts into a poem published the next day in the *Shanghai Daily* (<cite id="eafmd"><a href="#zotero%7C14298532%2FC92QNES9">(Gu Wu Lü’eguan zhu 古吳绿萼館主, 1887)</a></cite>):
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
> Take easy a dice bowl, set a square buffet.
> Imperial offices spread out, all play.
> Merit and fame, on paper, come like a dream.
> Good offices in fact are all up for pay.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
There is a double denial of realism in this poem. In line three, there is the dice game vs. the reality of official careers, one being easy and equitable, the other one hard to attain. Line four, by contrast, evokes the official career as it ought to be, neatly outlined in the voluminous administrative codes of the Qing dynasty, vs. the reality of widespread venality where official rank could simply be purchased, and even legally so.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"po69o": [{"id": "14298532/QNAXB5L3", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
This paper reflects a similar tension. Can we draw up any sort of relationship between the positions on the game chart and the dice-driven movements between them on one hand and the actual Qing bureaucracy on the other? Wouldn’t using the game to discuss real world situations be like using Monopoly to talk about the turn of the century American housing market? Yet, even if we assume the game chart purely as an imagined bureaucracy, we still do not know how it stood to lived reality. A mirror? A representation? A mockery? How contemporaries imagined the actual lived bureaucracy can only be gauged from poems like the one cited above. Can we know anything about the intentions of the anonymous game designer? Or should we be rather agnostic about these questions and study the game qua game? Games have largely been the domain of archeologists, art historians, anthropologists, and, more recently game studies. Historians of China have long been reluctant to take games seriously as an object of study (however, for a recent study of lotteries see: <cite id="po69o"><a href="#zotero%7C14298532%2FQNAXB5L3">(Li, 2023)</a></cite>). It has not least been the skepticism expressed by historians that has prompted us to give much more space to questions of historiography and historicity than we initially planned (readers more interested in the computational challenges are advised to skip [“Utopias of Rules”?](#anchor-section-4-*) and directly proceed to [Equal opportunity?](#anchor-section-5-*)). We still do not subscribe to historical agnosticism and continue to believe that we can find out how contemporaries imagined their bureaucratic system through a study of the game. Most prominently, how did they feel about career chances within a system that was increasingly rigged by venality during the nineteenth century? This section will, after brief literature review, outline our approach. In a nutshell, we will be talking about three bureaucracies: one depicted on the game chart, one outlined in imperial administrative statutes, and one as lived reality.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"851jv": [{"id": "14298532/5ZHJZ28C", "source": "zotero"}], "padzg": [{"id": "14298532/PQVWKAP3", "source": "zotero"}], "tdgcf": [{"id": "14298532/ZLCXSS4P", "source": "zotero"}], "yd709": [{"id": "14298532/LBBMUNK7", "source": "zotero"}]}} editable=true raw_mimetype="" slideshow={"slide_type": ""} -->
In fact, for better or worse, historians have long used Mandarin Promotions as a teaching device to instruct students about how the (idealized) Qing bureaucracy worked. In 1877, when the Bodleian Library obtained the 1840 game chart, the cataloger, none less than the eminent Sinologist James Legge, jotted on its back the words “official directory” (“Qing Guan Ce 清官冊”, see <cite id="padzg"><a href="#zotero%7C14298532%2FPQVWKAP3">(Helliwel, 2014)</a></cite>). Legge perhaps knew that it was a game and only failed to make a note, but we cannot know. May-ying Ngai cites the anecdote that Pao Chao Hsieh (Xie Baoqiao 謝保樵, 1896-1960), author of an influential English-language introduction to the bureaucratic system of the late Qing dynasty in 1925, used *Mandarin Promotions* to entertain fellow students and professors and was rumored to have based the book “on his favourite plaything” (<cite id="851jv"><a href="#zotero%7C14298532%2F5ZHJZ28C">(Ngai, 2010)</a></cite>, p. 3, fn. 3. The book is: <cite id="tdgcf"><a href="#zotero%7C14298532%2FZLCXSS4P">(Hsieh, 1925)</a></cite>.) Two thirds of Puk Win Kin’s reproduction of the game comprise of explanations of the actual working of the Qing bureaucracy, based on earlier work by Lu Yan 魯言 (1924-1995) and historical sources. Endymion Wilkinson in his famous reference work on Chinese history placed a note on Mandarin Promotions in chapter 3.17 “Central & Local Government,” not in chapter 24.14. “Sports & Games” (<cite id="yd709"><a href="#zotero%7C14298532%2FLBBMUNK7">(Wilkinson, 2012)</a></cite>). 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"1e7lr": [{"id": "14298532/CDULDIBZ", "source": "zotero"}], "7nswa": [{"id": "14298532/3JHDWAR9", "source": "zotero"}], "8t89v": [{"id": "14298532/KAWPABR8", "source": "zotero"}], "juveg": [{"id": "14298532/R6IGW83X", "source": "zotero"}], "sjx5i": [{"id": "14298532/G7HQLMZ7", "source": "zotero"}], "syz0k": [{"id": "14298532/P4MRZKFS", "source": "zotero"}], "u48f6": [{"id": "14298532/W9F7GZR6", "source": "zotero"}], "v2ryv": [{"id": "14298532/UCJTBZXX", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Bureaucratic promotion games have a long history in China. The oldest version, whose rules have survived in full, named Han Officials (Han Guan Yi 漢官儀), was created by Liu Ban’s 劉攽 (1022-1088) in the eleventh century AD to teach the bureaucratic system of the first century BC. Not only have educators used it as a teaching device for the study of the Western Han dynasty ever since. The game was even cited as historical evidence by later historians and hence created historical knowledge for generations of scholars (<cite id="v2ryv"><a href="#zotero%7C14298532%2FUCJTBZXX">(Zhang Mingwei 章名未, 2023)</a></cite>; <cite id="sjx5i"><a href="#zotero%7C14298532%2FG7HQLMZ7">(Lo, 2004)</a></cite>). The use of games as teaching devices is also not limited to China. The closest relatives of Mandarin Promotions, the Indian Game of Knowledge (which has inspired both Milton Bradley’s Checkered Game of Life and Snakes and Ladders) and the even more similar Tibetan Game of Liberation were both games of moral edification (<cite id="juveg"><a href="#zotero%7C14298532%2FR6IGW83X">(Schmidt-Madsen, 2019)</a></cite>; <cite id="1e7lr"><a href="#zotero%7C14298532%2FCDULDIBZ">(Tatz &#38; Kent, 1977)</a></cite>). European goose games and Japanese sugoroku games, the latter equally played during New Year’s festivities, could be adjusted as personal promotion games or to teach history, geography, and imperial conquest (<cite id="7nswa"><a href="#zotero%7C14298532%2F3JHDWAR9">(Seville, 2019)</a></cite>; <cite id="syz0k"><a href="#zotero%7C14298532%2FP4MRZKFS">(Groote et al., 2016)</a></cite>; <cite id="8t89v"><a href="#zotero%7C14298532%2FKAWPABR8">(Eubanks, 2016)</a></cite>; <cite id="u48f6"><a href="#zotero%7C14298532%2FW9F7GZR6">(Paget, 2017)</a></cite>).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"7vc69": [{"id": "14298532/C5VWSXW6", "source": "zotero"}], "db3hc": [{"id": "14298532/JVTS5CKH", "source": "zotero"}], "h0g3s": [{"id": "14298532/6GTU5NGL", "source": "zotero"}], "hjz2f": [{"id": "14298532/8B39GJMI", "source": "zotero"}], "s05vj": [{"id": "14298532/BXSXXT84", "source": "zotero"}], "znyuf": [{"id": "14298532/G7HQLMZ7", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Others have understood *Mandarin Promotions* as a social commentary and even critique. As early as in 1687, a Jesuit convert introduced the English librarian Thomas Hyde to the game, albeit in an earlier version that included civil and military officers and was played with six dice. Hyde not only used the game to introduce the Chinese bureaucracy to his audience; it also served him as proof that the Enlightenment idea of China’s bureaucratic rule by merit was a myth (<cite id="s05vj"><a href="#zotero%7C14298532%2FBXSXXT84">(Hyde, 1694)</a></cite>, 73; <cite id="db3hc"><a href="#zotero%7C14298532%2FJVTS5CKH">(Batchelor, 2014)</a></cite>, 224-226). In the 1970s, the anthropologist Leon Stover described the game in detail to make a grand sociological argument about nothing less than *The Cultural Ecology of Chinese Civilization*. Stover compared *Mandarin Promotions* to *Monopoly*. Instead of real estate and wealth, players compete for political power, because, as Stover put it, “in the Chinese Agrarian State. Power is the origin of wealth” (<cite id="hjz2f"><a href="#zotero%7C14298532%2F8B39GJMI">(Stover, 1974)</a></cite>, 215; <cite id="znyuf"><a href="#zotero%7C14298532%2FG7HQLMZ7">(Lo, 2004)</a></cite>, 66). Such claims are surely exaggerated. However, they are not alone. Decades before Charles Darrow plagiarized *Monopoly* and Parker Brothers turned it into a celebration of capitalism, the game was patented by Elizabeth Magie, a follower of Henry George, as the *Landlord’s Game* to uncover the evils of the monopolist housing market in the US (<cite id="7vc69"><a href="#zotero%7C14298532%2FC5VWSXW6">(Pilon, 2015)</a></cite>). In the early 1980s, in still Communist East Germany, Martin Böttgers invented a game *Bürokratopoly* to reflect in an ironic way on his society. Unconsciously mirroring Stover’s description of Qing China, Böttger later motivated his shift away from *Monopoly*’s money nexus by the political realities of a communist state: „In a centralized bureaucracy of functionaries, like the GDR, it was the pursuit of social advancement, of power, that held the system together” (<cite id="h0g3s"><a href="#zotero%7C14298532%2F6GTU5NGL">(DDR-Museum, 2018)</a></cite>). In a quirky detour across a game board, sociological analysis and political comment found similarities between Qing China and Communist East Germany: Power had won over wealth. Thirtyfive years after the collapse of the East German communist state, *Bürokratopoly* is still marketed to schools by the DDR Museum to make students in the FRG (1949-today) understand life in the GDR (1949-1990), which also no longer exists, much like the game *Han Officials* recreated Han China (202BC-220AD) for Song (690-1276) people and *Mandarin Promotions* recreates Qing China (1644-1911) for people living in today’s Sinophone communities. If the *Landlord’s Game* and *Bürokratopoly* were created with didactic intent, so was Mandarin Promotions (we will cite evidence in [“Utopias of Rules”?](#anchor-section-4-*)). How can we study this historical board game as a historian then?  
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"3j0lf": [{"id": "14298532/VIW5D949", "source": "zotero"}], "d7frx": [{"id": "14298532/NSGHLJTT", "source": "zotero"}], "jibuj": [{"id": "14298532/6SYD6Z2W", "source": "zotero"}], "koke9": [{"id": "14298532/BXSXXT84", "source": "zotero"}], "lmdn7": [{"id": "14298532/SF8BLY5P", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Some of our inspiration comes from sociologists and anthropologists who have been more open to crossing the line between game and society, ever since Johan Huizinga has famously made play into a field of serious academic study (<cite id="d7frx"><a href="#zotero%7C14298532%2FNSGHLJTT">(Huizinga, 1950)</a></cite>). Roger Caillois subsumed play and games under four categories—agon (competition), alea (chance), mimicry (simulation), and ilinx (vertigo)—and applied these categories freely to society. Since modern societies suppress the latter two, he argues, modern political systems are left with a precarious equilibrium between agon (merit, competition) and alea (chance, inheritance, lot) (<cite id="jibuj"><a href="#zotero%7C14298532%2F6SYD6Z2W">(Caillois, 2001)</a></cite>, 109-110). The applicability of this idea to a competitive career game appears obvious. But the remarkable fact that *Mandarin Promotions* almost entirely relies on alea or chance already irked Thomas Hyde whose early Enlightenment contemporaries firmly believed that Chinese officials were recruited by meritocratic competition (<cite id="koke9"><a href="#zotero%7C14298532%2FBXSXXT84">(Hyde, 1694)</a></cite>, 73). Bourdieu has made copious use of the game metaphor to explain how people operate within social fields by getting “a feel for the game,” although he believed that they are more successful if they are quasi born into it, making the social game an unequal one (<cite id="3j0lf"><a href="#zotero%7C14298532%2FVIW5D949">(Bourdieu, 1990)</a></cite>, 66-68 and passim). David Graeber, by contrast, considered the game a “utopia of rules,” a sheltered space where rules exist and are known to all participants, so that an equal playing field becomes possible (<cite id="lmdn7"><a href="#zotero%7C14298532%2FSF8BLY5P">(Graeber, 2015)</a></cite>, 189-191). In Seligman’s terms, games are subjunctive worlds where players find equal playing fields that are absent from their lived experience (we will have to explore whether this is true for Mandarin Promotions). Graeber has described the intrusion of rules even into anti-bureaucratic phantasies like *Dungeons & Dragons* as a process of bureaucratization, calling rule-based games a “bureaucratic fantasy.” At the same time, bureaucracies themselves also create games, i.e. rule-based playing fields, “they’re just games that are in no sense fun” ((Graeber, 2015), 190). In *Mandarin Promotions*, as we will show, the two come together, but they still are fun.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"o0i7g": [{"id": "14298532/VRXHV5XJ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We think that it is not too far-fetched to see *Mandarin Promotions* as a form of mimicry, as it simulates the career-making process quite faithfully from the Imperial examinations to the triennial performance reviews. On one hand, as we will demonstrate, the game is so dense in context that it would not have been playable without a thorough understanding of the bureaucratic institutions of the Qing. We would also be unable to analyze it without frequent reference to these institutions. *Mandarin Promotions* cannot be studied as game qua game. At the same time, we argue that *Mandarin Promotions* was a mimicry, not of the lived bureaucracy in Qing China, but of the statutory bureaucracy. The statutory bureaucratic system, outlined in imperial statutes and regulations, established an ideal of how the Qing bureaucracy was supposed to operate (<cite id="o0i7g"><a href="#zotero%7C14298532%2FVRXHV5XJ">(Metzger, 1983)</a></cite>), hence an “utopia of rules.” By the time our game was created on the basis of the Imperial statutes, in 1840, it had already become almost as far from reality on the ground as the game board itself. The double dissonance of our poet in the beginning of this section mirrors this fact. 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"xbhtm": [{"id": "14298532/PB9GMRPC", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Central to our approach to the game is hence to draw a careful distinction between three bureaucracies: first, there is the game bureaucracy, the system as modeled in *Mandarin Promotions*; second, there is the statutory bureaucracy, the idealized career ladders outlined in official regulations. Our comparisons in this paper are between the game and statutory bureaucracies. Each in its own way, both represent the Qing “ladder of success” as they unfold “on paper,” one as a subjunctive “as if” world, the other as a bureaucratic ideal that the empire aspired to live up to (<cite id="xbhtm"><a href="#zotero%7C14298532%2FPB9GMRPC">(Ho, 1980)</a></cite>). Hence, we treat the game bureaucracy as an imagination of this bureaucratic ideal, without ignoring the didactic intent of the game designer, as expressed in his preface printed on the game board. At the same time, we treat the statutory bureaucracy not as a perfect reflection of reality, but as a “utopia of rules” in its own right.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"as3yr": [{"id": "14298532/8QEMK6W6", "source": "zotero"}], "cih6b": [{"id": "14298532/RISMH8PS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The third bureaucracy is the actual lived bureaucracy, as shown in career patterns lived by real men that have been reconstructed from primary sources by many scholars, and collected in biographical databases like the China Biographical Database Project (CBDB, <cite id="cih6b"><a href="#zotero%7C14298532%2FRISMH8PS">(Harvard University et al., 2025)</a></cite>) or the Chinese Government Employee Database-Qing (CGED-Q; <cite id="as3yr"><a href="#zotero%7C14298532%2F8QEMK6W6">(Campbell et al., 2025)</a></cite>). The lived bureaucracy could hardly be pressed into a game board, albeit not for lack of trying (Liu Ban’s *Han Officials* did add historical biographies to his game description). *Mandarin Promotions* does not reflect this lived bureaucracy, and it will not be the subject of this paper. However, as we will see, reality crept into the game through the introduction of office purchase. This institution was an innovation in the 1840 game board compared with earlier versions; it also was the only facet that kept developing on the later boards. “Good offices in fact are all up for pay” was a reality that Qing people did have to reckon with, in life and in the game.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
After explaining the basic set-up of the game and our approach to modelling it in the next section ([Introducing the Game and our Data Model](#anchor-section-3-*)), we will show in [“Utopias of Rules”?](#anchor-section-4-*) how the game recreated the statutory system and how it creatively imbued it with value judgement. [Equal opportunity?](#anchor-section-5-*) will then look at the entry, i.e. the different starting positions, to show how the game was not entirely contrived as an equal playing field.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-3"] -->
## Introducing the Game and our Data Model¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### The Game Chart as an Imperial Metaphor¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
*Mandarin Promotions* (*Shengguantu* 陞官圖) belongs to the family of “life games” that model the progression of human existence or moral salvation, such as the Indian *Game of Knowledge* (perhaps one of the ancestors of Milton Bradley’s *Checkered Game of Life*), the Tibetan *Game of Liberation*, or the European *Game of the Goose*. Yet *Mandarin Promotions* is neither a moral journey nor a simple race of chance. The chart ([Figure 1](#figure-game-chart-*)), courtesy of Puk Wing Kin) represents the bureaucratic universe of the Qing Empire as a spatial metaphor of hierarchy and order.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-game-chart-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Game chart with compartment numbers"
            ]
        }
    }
}
display(Image("media/game_chart_numbers.png"), metadata=metadata)
```

<!-- #region citation-manager={"citations": {"79rye": [{"id": "14298532/85FJBBY2", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The layout is circular and concentric, resembling a monarchic cosmos: the emperor is in the center (but outside of the game proper), surrounded by successive circles representing the court, the capital bureaucracy, and the realm (<cite id="79rye"><a href="#zotero%7C14298532%2F85FJBBY2">(Duindam, 2015)</a></cite>, 5). The throne occupies the metaphysical apex of this order—an absent but omnipotent presence. In earlier or simplified versions, the center depicted the Forbidden City’s gate, the symbolic access to the emperor. In the nineteenth-century chart reproduced here, the central square instead contains the printed game rules and serves as the space to place the bowl into which dice are thrown. The throne thus exists “above” the game, invisible yet determining the players’ fates through dice rolls—a deus ex machina of bureaucratic destiny
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
From the rim toward the center, sixty-six departments are arranged in three main circles. These departments correspond to real Qing bureaucratic institutions: The outer ring contains the chushen starting positions, the civil service examinations (C3–C6), the system of promotions and penalties, and the provincial administration including prefectural and county offices (C19, C15). The second ring contains the metropolitan administration including the six ministries (C32–C37) and related boards in Beijing. The third ring closest to the imperial center contains court titles as well as honorary titles and rewards (C60, C63–C64).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In total, 434 positions are distributed across these 66 departments. The goal—department C66, Examination of Rank-Classes (*pinjikao* 品級考)—lies near, but not in, the center. The throne itself is unreachable: the emperor remains beyond the game chart, as the arbiter of fortune. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-32-*"] -->
### Playing Mandarin Promotions¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
*Mandarin Promotions* is a board game played with dice—in our version four—by any number of players. In our simulation in [Equal opportunity?](#anchor-section-5-*), we assume four players.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### Starting the Game: *Chushen* and Hereditary Titles
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Unlike other life games with a single point of “birth” or “go,” Mandarin Promotions begins outside the chart. The first throw of dice determines one’s initial social status. There are twenty-two possible entry points distributed between two outer departments: C1, *Chushen*, with fifteen positions, and C2, *Hereditary Nobility*, with seven.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The fifteen *chushen* starting positions represent various social origins or educational credentials. Only three correspond directly to degrees obtained through the civil service examinations (two of them could also be purchased), while the rest symbolize other forms of qualification or privilege (for details see [Table 7](#table-41-*) below). The seven noble titles in department C2, among them P16 Sacred Prince (*yanshenggong* 衍聖公), a title given to direct descendants of Confucius, and several Manchu titles, are attainable only with “lucky” dice—that is, four identical numbers. Such a throw has a probability of less than 0.08 percent ((⅙)⁴), underscoring the rarity of hereditary privilege.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In the symbolic logic of the chart, social origins are spatially encoded: chushen positions occupy the outermost rim, the periphery of the empire; hereditary nobility lies closer to the center, within the ring of court offices. From the start, the game world is not egalitarian but hierarchical, reproducing the structure of the Qing polity itself.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-23-*"] -->
#### Movement and Dice Combinations
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Like most life games, *Mandarin Promotions* is driven by dice rather than strategic choice. The game uses four dice, whose red faces (ones and fours) indicate the worst and best numbers, as in other Chinese dice traditions. From each position, six possible target squares are specified in smaller characters beneath the main title, so that each dice result corresponds to a particular move. The result is a dense network of instructions rather than a linear path. For an unfamiliar viewer, all positions with their follow-up instructions look similar, but they are not. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
There are twenty-five basic dice combinations: six each for two-equals (doubles), three-equals (triples), all-equals (*quanse* 全色), and one special straight 3-4-5-6 (*chuanhua* 穿花, “garland”). Double combinations are endowed with symbolic, meritocratic meaning and are not read numerically but numinously: Double-4, *de* 德, Virtue (the best combination); Double-6, *cai* 才, Talent; Double-5, *gong* 功, Effort; Double-3, *liang* 良, Mediocre; Double-2, *rou* 柔, Weak; Double-1, *zang* 賍, Corrupt (cancelled by a 4).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"wzq2n": [{"id": "14298532/VKHBKXRB", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Triples (only used to access starting positions), all-equals, and the garland (3-4-5-6) are “lucky” throws and ensure unusually rapid promotion. Double-1 and triple-1 are disastrous, yet a single 4 in the combination can avert their misfortune. Fate, not strategy, defines merit; yet by assigning moral value to chance, the game transforms the randomness of dice into a symbolic representation of the Qing meritocracy (<cite id="wzq2n"><a href="#zotero%7C14298532%2FVKHBKXRB">(Elman, 2013)</a></cite>).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### Money, Wagers, and Office Purchase
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
*Mandarin Promotions* (in its nineteenth-century version) was played both for rank and for money. At the start, each player contributes 100 chips to a common pool. Money moves throughout the game according to instructions printed on the chart:
- Rewards: payments from pool to player.
- Fines or purchases: payments from player to pool.
- Gifts: payments from one player to another.
The pool thus functions as a miniature economy: even though the initial amount is fixed, money circulates and multiplies through transactions. At the end of the game, any remainder in the pool is distributed in proportion to players’ final ranks, with lower-ranking players paying out higher-ranking ones.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The most consequential rule printed in the center of the board permits the purchase of office (*juan* 捐). The specifics of timing and cost are deliberately vague, leaving the decision to the players’ discretion. Because all other moves are determined by dice, purchase becomes the only moment of agency — a space for strategy within the fateful order. Whether buying rank is a rational choice is an issue examined in [Equal opportunity?](#anchor-section-5-*).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### Climbing the Ladder
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
To enter the game proper, each player’s first throw assigns a *chushen* position, making the player eligible for bureaucratic service. From this point onward, movement is determined by the combination of dice rolled at each turn and the instruction attached to the current position. The aim is to rise through nineteen rank-classes, from 9b (lowest) to 1a (highest), and eventually to retire with honor in the final department C66, Examination of Rank-Classes. The rank attained at retirement equals the level of the last office held. Retirement may occur under different circumstances—honorable (*he* 賀 or *dahe* 大賀), notified ((yugao* 予告), or dismissed (*xiuzhi* 休致) — which affect the player’s final rewards.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Of the 434 total positions, 338 are accessible to the player’s main piece. These include all chushen entries, noble titles, examination stages (26), and ranked offices (272). The latter represent vacancies (*que* 缺), which were strictly limited in number by statutory law while actual personnel was rotated through them. However, the game bureaucracy is not proportional to the statutory bureaucracy. In the former, 190 positions represent metropolitan vacancies and 82 provincial ones, resulting in an overrepresentation of Beijing. For example, the chart lists two county magistrate positions (*zhixian* 知縣, 7a), one for a “busy” and one for a “simple” county, even though over 1,300 counties existed in reality, each with a magistrate. Conversely, the game shows only one Minister of Revenue (*hubu shangshu* 戶部尚書, 1b), while the statutory bureaucracy maintained two (one Manchu, one Han).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### Temporary Positions and Special Rules
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Ninety-six positions on the game chart are designated as temporary and require a secondary marker, which remains on the temporary square while the main piece holds its place. On the following turn, the dice result is applied according to the instruction of the temporary square, after which the marker is usually withdrawn. These temporary mechanisms — comparable to the “snakes” and “ladders” in the eponymous European game — add complexity and realism.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
They correspond to three institutions in the Qing bureaucracy:

- Performance Reviews (*kaohe* 考核): triennial evaluations for provincial officials (C12 *Daji* 大計, “Great Reckoning”) and for metropolitan officials (C10 *Jingcha* 京察, “Capital Evaluation”). Also included are the departments for military merit (C9 *Jungong* 軍功) and penalties (C13 *Chufen* 處分). A “corrupt” dice roll (Double-1) can send a player directly into C13. (25 positions total.)
- Commissions (*Chaishi* 差使): temporary assignments or missions during which the main post is suspended. (38 positions total.)
- Honorary Rewards and Titles: imperial honors and decorations, such as *Hualing* 花翎 (peacock-feather plume decoration, P413), titles of higher nobility (C63), or palace titles (C60 *Taizi Taibao* 太子太保, “Grand Protector of the Heir Apparent”). (33 positions total.)
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
#### Memory and Eligibility
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Certain promotions or transfers are conditional upon having previously visited particular positions. This introduces a “memory” mechanism into the game, preventing purely Markovian play. For example, only players who have previously “become Manchu” by visiting a Manchu position may advance to Assistant Grand Secretary (*Xieban Daxueshi* 協辦大學士, 1b). These prerequisites replicate the importance of hereditary status, ethnicity, and credential in real Qing officialdom and significantly complicate digital modeling of the game.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Translations

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"5qud9": [{"id": "14298532/J5HSXH8H", "source": "zotero"}], "c003w": [{"id": "14298532/G7UZDYUU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
For the translation of official titles and institutions, this study follows Charles Hucker’s *Dictionary of Official Titles* (1985) because of its wide use in digital-humanities projects, even though it is less precise for the late Qing (<cite id="5qud9"><a href="#zotero%7C14298532%2FJ5HSXH8H">(Hucker, 1985)</a></cite>). Where late-imperial nuances are essential, Brunnert and Hagelstrom’s *Present Day Political Organization of China*)(1912) provides more accurate equivalences (<cite id="c003w"><a href="#zotero%7C14298532%2FG7UZDYUU">(Brunnert &#38; Hagelstrom, 1912)</a></cite>). To avoid confusion for Chinese-reading audiences, original Chinese names are retained; where space allows, bilingual tables are provided.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-34-*"] -->
### Career paths as network and tree¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Based on its characteristics, it is possible to re-imagine *Mandarin Promotions* as a network, in which the positions are the nodes and the dice rolls are the edges. Chushen starting positions only have one incoming edge (from outside the game). Final positions have no outgoing edges. All other positions can only have up to six outgoing edges, but should be expected to have at least one incoming edge (in reality, they often have many more). However, there are in fact positions in the game that have no incoming edges, namely the grace tribute student (C3-學院 : P29-恩貢) and the annual tribute student (C3-學院 : P30-歲貢), both part of the examination system. That is, the game designer did not include any rule to move to these positions, so that nobody can ever get there. Our hypothesis is that the game designer aimed for completeness in his representation of available positions in the statutory system, but could not come up with a dice move, because he was constrained by the limit of six outgoing edges per position.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The network structure obtained in this way is not a social network, of course, but rather resembles a transport network where the career paths are routes through the nodes, and nodes with many incoming paths are important positions that, over several playthroughs of the game, many players will pass through in their careers. Strictly speaking, these career paths only lead through 338 nodes, while the 96 temporary positions for the secondary game piece are modelled as additional states of the main nodes. However, the latter can also be understood as a furlough between position — go to position x and wait until a decision for your next move. When Elisabeth Kaske first conceived of the game in network terms, the treatment of these temporary positions posed considerable trouble. When she implemented the network in Neo4J, she made the decision to distinguish between the two types of nodes by imposing a uniqueness constraint on the 338 regular nodes (hence dubbed “uniquenodes”) while new temporary nodes were created each time for the temporary positions (hence dubbed “concurrentnodes”). This pushed up the total number of nodes to over 4,000 which complicated the resulting network graph, creating in a hairball effect, i.e. an overly dense structure, but it rendered a precise representation of the game moves.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
A condensed version of the resulting graph is shown in [Figure 2](#figure-32-*), grouping positions into clusters based on their type (e.g. starting positions “Start”, positions having a rank “Ranked” and so on). Edges represent dice rolls. MERIT stands for doubles. LUCK stands for four equals, 3-4-5-6, 11-44 etc., i.e. dice rolls with lower probability):
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
Since Neo4J proved too unwieldy to be handled for further analysis, Elisabeth Kaske exported the data to Gephi. This method yielded valuable results for historical comparison which will be discussed in [“Utopias of Rules”?](anchor-section-4-*). However, the simple network approach had limits. First, Gephi is built to study social networks and thus does not perfectly fit the game, which only uses directed edges and can be most fruitfully studied with methodology for transport networks. Secondly, a network graph also could not accurately answer our question if all of the fifteen starting positions in the “chushen” category (not considering the seven positions of hereditary nobility) have the same opportunities in the game. As explained above, the game mimics the statutory system by forcing the player to keep track of status inherited or obtained previously. Some positions higher up in the hierarchy represented in the game are hence limited to people having visited a particular position earlier in the game. Using a network as the model, it is difficult to study such rules relying on memory. Thirdly, calculating monetary gain or loss also proved difficult.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Here is where a programmatic approach proved superior. Based on the existing data in the Excel worksheet and a new reading of the rules, Florian Keßler has implemented the game in Python, making it possible to study it using a Monte Carlo approach by simulating a large number of playthroughs to determine competitive chances and monetary gains. To simulate strategic choice in office purchase, Florian Keßler adopted a classical method from artificial intelligence, that decides for or against purchase based on the highest gain after a fixed number of simulated playthroughs for each of the many possible choices, giving a rough version of a Monte Carlo Tree Search. The results of this exploration will be discussed in [Equal opportunity?](#anchor-section-5-*).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-4-*"] -->
## “Utopias of Rules”? The Real and the Gamified Qing Bureaucracy
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Official Rules: The Examination of Rank-Classes
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
If we argue that Mandarin Promotions is both mimicry of and a comment on the statutory bureaucracy, we have two types or sources to find out specifics. One is statements of game designers or players. The other is the game design itself. For comparison, we also need to consider the sources of this game design which lead us to better understand the relation to the (statutory) bureaucracy. 
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"bhkhf": [{"id": "14298532/V8FFRKCS", "source": "zotero"}], "hz9wh": [{"id": "14298532/5ZHJZ28C", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We have cited player opinion in the poem at the beginning of [Can we study a historical board game as historians?](#anchor-section-2-*). The game board itself contains a preface of the anonymous game designer which states the following: “Based on the *Collected Statutes* (*Huidian* 會典), we have made a comprehensive table of official ranks, complete for Manchu and Han officials, and differentiated between the regular and irregular paths. It is not just a game, but faithfully lets the distinctions of official ranks and the understanding of their qualifications be clearly spread out in one table, in order to be of great service” (<cite id="bhkhf"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>, 22; for a full, but slightly different translation see: <cite id="hz9wh"><a href="#zotero%7C14298532%2F5ZHJZ28C">(Ngai, 2010)</a></cite>, 76).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"7ntjh": [{"id": "14298532/7VKH8LPN", "source": "zotero"}], "iosj9": [{"id": "14298532/LBBMUNK7", "source": "zotero"}], "p9omr": [{"id": "14298532/CWESQSGQ", "source": "zotero"}], "zj54t": [{"id": "14298532/IJAXKZ39", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
That designer did not cite his name does not mean that we cannot know anything about him. He was obviously highly literate and well-versed in Qing administrative laws. With all likelihood, he belonged to the scholar-official circles about which a whole lot is known. In any case, his defensive rhetoric (“it is not just a game”) is clearly directed at these circles. He, first, declares that *Mandarin Promotions* is an accurate reference work reflecting the contemporary bureaucratic system. He, secondly, manifests faithfulness by citing the major compendium of Qing administrative law (<cite id="7ntjh"><a href="#zotero%7C14298532%2F7VKH8LPN">(Keliher, 2016)</a></cite>. For the translation of the term “huidian” see: <cite id="iosj9"><a href="#zotero%7C14298532%2FLBBMUNK7">(Wilkinson, 2012)</a></cite>, 843. This reference work (pp. 253-268) also contains the best concise introduction into the structure of the Qing bureaucracy.). Thirdly, he claims comprehensiveness by including the major status distinctions between Manchus and Han, as well as different “paths” into officialdom. What he refers to as “regular path” mainly refers to the imperial examinations. The “irregular path” mainly refers to office purchase, referred to by the poet in [Can we study a historical board game as historians?](#anchor-section-2-*), which was perfectly legal albeit “irregular” (<cite id="p9omr"><a href="#zotero%7C14298532%2FCWESQSGQ">(Elman, 2000)</a></cite>; <cite id="zj54t"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"hswd4": [{"id": "14298532/54772HN8", "source": "zotero"}], "vh6v9": [{"id": "14298532/SLU49A89", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The *Collected Statutes* mostly contain regulations and imperial decisions on specific cases (“*shili* 事例” which were collected as “*Huidian shili* 會典事例”). To make these into a game would have been a daunting task. Fortunately, the Collected Statutes also contain chapters titled “Examination of Rank-Classes.” Their Chinese name is “*Pinji Kao* 品級考”, and this is also the name of the department on the game chart which marks the final goal of the game. Chapters titled “Examination of Rank-Classes” were also collected in other administrative compendia, especially of the Ministry of Personnel, and circulated as separate booklets (<cite id="hswd4"><a href="#zotero%7C14298532%2F54772HN8">(Will, 2020)</a></cite>, 120-121. Our translation of the title is more literal than Will’s, because we wanted to highlight the emphasis on the system of numeric rank-classes.). The goal of these regulations was to create a rational and stable framework for personnel promotions that limits arbitrary acts arising from patronage relationships (<cite id="vh6v9"><a href="#zotero%7C14298532%2FSLU49A89">(Wu Yue 伍跃, 2021)</a></cite>, 2021, 255). Given that *Mandarin Promotions* has been mistaken for an “official directory,” it is necessary to bring in such an official bureaucratic promotion chart for comparison.

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"7hjhz": [{"id": "14298532/54772HN8", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
As the main outline of regular career promotions the statutory bureaucracy, the “Examination of Rank-Classes” (below “Examination”) contains a list of over 200 official designations which are arranged by their assigned rank-class from the highest rank-class to the lowest. There were 9 ranks (*pin* 品) with 18 rank-classes (*ji* 級), hence “*pinji*,” plus one unclassed (*weiruliu* 未入流), making 19 which are habitually numbered 1a to 9b, plus “unclassed” (10 in our encoding). More importantly, the “Examination of Rank-Classes” also contains orderly steps from lower ranks up to higher ranks. In other words, each office can only be recruited from a limited number of lower-ranking offices and be appointed to a limited number of higher-ranking offices. The foremost student of the Qing administration outside China, Pierre-Étienne Will, has observed that “the same content is also found in … tables called Shengguan tu 陞官圖, Baiguan duo 百官鐸, and other names, that were popular from the Ming through the Republican periods (and were adapted in Japan taking account of local institutions), and served as a support for a game played with dice” (<cite id="7hjhz"><a href="#zotero%7C14298532%2F54772HN8">(Will, 2020)</a></cite>, 121). In other words, the “Examination” was the ideal material for gamification. So, how is Mandarin Promotions related to these chapters?
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"wk7ue": [{"id": "14298532/LBBMUNK7", "source": "zotero"}], "xx3oh": [{"id": "14298532/G9J8Z9FU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
As a proof of concept, we may use a network to inspect an “Examination” chapter. The Collected Statutes were updated from time to time, so there are five editions throughout the Qing. The editions closest to 1840 were printed in 1768 and 1823 (<cite id="wk7ue"><a href="#zotero%7C14298532%2FLBBMUNK7">(Wilkinson, 2012)</a></cite>, 843). We have had only the edition of 1768 at hand, but research has shown that changes in “Examination” were slight (<cite id="xx3oh"><a href="#zotero%7C14298532%2FG9J8Z9FU">(Wu Yue 伍躍, 2022)</a></cite>). As we will see below, the big change also came in 1843, i.e. after the game chart was created, so this may be acceptable. Elisabeth Kaske digitized this edition and compiled it into a source-target table, which she then entered into Gephi and analysed the graph by applying modularity and betweenness centrality algorithms. This procedure yielded the following graph ([Figure 3](#figure-321-*), Chinese, and [Figure 4](figure-321-transl-*), English):
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-321-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Examination of Rank-Classes (Chinese)"
            ]
        }
    }
}
display(Image("media/Figure 3.2.1. PJK_chin.png"), metadata=metadata)
```

```python editable=true slideshow={"slide_type": ""} tags=["figure-321-transl-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Examination of Rank-Classes (English)"
            ]
        }
    }
}
display(Image("media/Figure 3.2.1. PJK_Trsl.png"), metadata=metadata)
```

<!-- #region citation-manager={"citations": {"uaz7p": [{"id": "14298532/WB58FURK", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
This graph (Figures [3](#figure-321-*) and [4](#figure-321-tranls-*)) first shows a high degree of modularity which is not a fact widely known about the Qing bureaucracy. Modularity (or community detection) is defined as “decomposing the networks into sub-units or communities, which are sets of highly interconnected nodes” (<cite id="uaz7p"><a href="#zotero%7C14298532%2FWB58FURK">(Blondel et al., 2008)</a></cite>, 2). We may remind the reader that this is not a social network. Clustered areas do not mean that officials of these types socialized more with each other than with others. Rather, as in a transport network, communities show areas more densely connected by career paths and distinguish them from other areas which are more distantly connected.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"6take": [{"id": "14298532/XQEIL32V", "source": "zotero"}], "ahwsk": [{"id": "14298532/B4HFQQLN", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Even though modularity is not a precise measure, the data show some revealing features of the statutory bureaucracy (see [Table 1](#table-1-*) for Gephi analysis results and graph). Three small clusters stand out whose members also have low betweenness centrality (see below). These are the officials at the Imperial Academy of Medicine (*taiyiyuan* 太醫院, modularity class 3), the Directorate of Astronomy (*qintianjian* 欽天監, mc 4), and those officials task with ritual music at the Court of Imperial Sacrifices (*taichangsi* 太常寺, mc 6). As specialized workers, the men employed in these institutions could be classed as “incipient professionals,” but they led isolated cul-du-sac careers. On the extremes of the graph, we find the lowest-ranking (8a to unclassed) provincial bureaucrats clustered in the lower corner (modularity class 5). They are worlds apart from an isolated upper-level court bureaucracy in the capital Beijing (upper right, class 0). Governors (*xunfu* 巡撫) and circuit intendants (*daoyuan* 道員) are the only provincial offices included in this group. A reference to the lived bureaucracy is necessary here. The names of all appointed officials were listed in quarterly official directories (*jinshenlu* 縉紳錄) and published four times every year. These official directories have now been compiled into the Chinese Government Employee Database-Qing (CGED-Q) by the Lee-Campbell group. Chen Bijia’s research on this data has shown that Beijing’s bureaucracy was staffed quite differently from the provincial bureaucracies, one consisting predominantly of Manchus and examination graduates, the other was crowded by Han officials and office purchasers with low mobility between them (<cite id="ahwsk"><a href="#zotero%7C14298532%2FB4HFQQLN">(Chen, 2019)</a></cite>. For the database: <cite id="6take"><a href="#zotero%7C14298532%2FXQEIL32V">(Chen et al., 2020)</a></cite>). Now we can confidently argue that this difference was related to the systematic setup of the statutory system. However, the most prosperous modularity class (2) of the network graph with most members (60, only counting those with non-zero betweenness centrality) and highest betweenness centralities, would also fall in that category, and their membership is mixed indicating (at least statutory) mobility between positions in Beijing and the provinces.
<!-- #endregion -->

```python editable=true jdh={"module": "object", "object": {"source": ["Examiniation of Rank-Classes (Modularity)"], "type": "image"}} slideshow={"slide_type": ""} tags=["table-1-*", "data-table"]
import pandas
pandas.read_csv("script/Table 1 PJK_Gephi_Analysis_Modularity.csv")
```

<!-- #region citation-manager={"citations": {"7ag6r": [{"id": "14298532/C62Y2KVY", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Graph theory knows many types of centralities. In accordance with our metaphor of a transport network, we chose betweenness centrality as the defining indicator of the importance of a position, because it measures the number of shortest career paths that pass through this position. “Betweenness Centrality is [also] a way of detecting the amount of influence a node has over the flow of information or resources in a graph. It is typically used to find nodes that serve as a bridge from one part of a graph to another” (<cite id="7ag6r"><a href="#zotero%7C14298532%2FC62Y2KVY">(Needham &#38; Hodler, 2019)</a></cite>, 97). In our projection, these positions were major hubs and bridges between distinct segments of the rank system. Hence, they can be considered pivotal for the career of officials. Betweenness centralities are clearly linking communities, with the county magistrate (*zhixian* 知縣, 7a, in modularity class 2) having the highest centrality between low- and mid-level positions, while the vice department director (yuanwailang 員外郎, also class 2) and investigating censor (*jiancha yushi* 監察御史, modularity class 0), both rank-class 5b, link to the higher court offices in the capital.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-42-*"] -->
### Game Rules: Plotting Mandarin Promotions
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"wfhse": [{"id": "14298532/JDFA84RJ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Theoretically, centralities could help to compare Mandarin Promotions to official regulations. Unfortunately, this proved impractical. To be sure, all office designations listed on the game chart do exist in various bureaucratic regulations of the Qing with exactly the correct names. However, they exist nowhere in the same combination.
First, “Examination” alone came in four versions for various ethnic status groups in the Qing bureaucracy: Han, Manchu, Mongols, and Han bannermen (for these status distinctions see: <cite id="wfhse"><a href="#zotero%7C14298532%2FJDFA84RJ">(Porter, 2023)</a></cite>). The game designer, by contrast, combined Han and Manchu. Secondly, the “Examination” chapters contain mostly ranked offices and the paths between them, plus a handful of chushen credentials. They are comparatively simple. (*Mandarin Promotions*), by contrast, contains official posts, but also the important chushen credentials, examinations, temporary commissions, honorific titles and titles of nobility, and even imperial rewards and baubles. The game creates additional suspense by letting players pass through the hoops of a simulated review process, getting promotions for excellence and demotions for failures. As a result, there are many more positions in the game than in any of the four “Examination” chapters. Thirdly, as stated above, the game chart overrepresents metropolitan offices (i.e. those in the Imperial and Court administration located in Beijing). More precisely, these offices are more differentiated than in “Examination.” For example, the county magistrate distinguishes “busy” and “simple” counties. The differentiation is even more pronounced in the metropolitan offices. A concrete example from the Six Ministries will be shown below in [Value: The Case of Ministries](#anchor-subsection-44-*). As a result, provincial offices have a higher mathematical centrality in the complete graph. Fourthly, the game designer had to be concerned with symmetry. Since the game was played by dice, each position has only six options for the next step, in network-speak it has an out-degree of at most 6. This was different from real promotion options, of course. Finally, results may be skewed due to decisions made by the researcher when she set up the data model, most prominently the inclusion of a Commoner position outside the game chart, before the player obtains a chushen with their first roll of dice, as well as the final positions, which only reckon the rank-class of the last position a player held by the end of the game.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The following graph ([Figure 5](#figure-322-*), Chinese, and [Figure 6](#figure-322-transl-*), English) plots modularity (color) and betweenness centrality (size of label) in Mandarin Promotions, in a similar way as Figures 3 and 4 above did for the “Examination” chapter. To avoid the hairball effect, the graph is filtered by cutting out nodes with extremely high (the Commoner) and low (most if not all of the temporary nodes, the remaining ones are nameless — NA — in the graph) betweenness centrality. As the previous graph, this one, too, is produced in Gephi using the projection Force Atlas.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["figure-322-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Mandarin Promotions (Modularity and Betweenness Centrality, Chinese)"
            ]
        }
    }
}
display(Image("media/Figure 3.2.2. SGT v.4 filtered chin.png"), metadata=metadata)
```

```python editable=true slideshow={"slide_type": ""} tags=["figure-322-transl-*"]
from IPython.display import Image
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Mandarin Promotions (Modularity and Betweenness Centrality, English)"
            ]
        }
    }
}
display(Image("media/Figure 3.2.2. SGT v. 4 filtered trsl.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
As discussed above, the greater differentiation of positions creates very different centralities and modularity classes. We cannot expect to replicate the results of the “Examination.” Provincial positions have a much higher centrality, especially the Provincial Surveillance Commissioner (P140, *anchashi* 按察使, rank-class 3a) and the two prefects (*zhifu* 知府, 5b, busy and simple P117, P118).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Nevertheless, we do see parallels to “Examination” in the global structure of the game bureaucracy. One is the clustering of the lowest-ranking provincial officials at the bottom (modularity class 17, see Table 2), albeit not as clear-cut as in the “Examination,” as well as the clustering of high-ranking court offices in Beijing at the other end (mc 1 and 22). There is also a large mixed field of Beijing and provincial official in the middle (mc 8, 16, 20). Finally, in Mandarin Promotions we find the same isolated cul-du-sac careers in the Royal Directorate of Astronomy (C40, *qintianjian* 欽天監) and the Imperial Academy of Medicine (C39, *taiyiyuan* 太醫院) in modularity classes 18 and 19. Following the game rules, students of astronomy and medicine were the most undesirable chushen starting positions. Original rules on the 1840 game chart stipulated that players landing on these positions should rather seek to bail themselves out by purchase, and these rules were even toughened on the later game chart (see [Equal opportunity?](#anchor-section-5-*)). This could be seen an expression of a value system that cherishes noble status and examination virtue over professional work.
<!-- #endregion -->

```python editable=true jdh={"module": "object", "object": {"source": ["Mandarin Promotions (Modularity and Betweenness Centrality)"], "type": "image"}} slideshow={"slide_type": ""} tags=["table-2-*", "data-table"]
pandas.read_csv("script/Table 2 SGT2_Gephi_Analysis_Betweenness_Modularity.csv")
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
In addition, the game shows two more isolated clusters among metropolitan officials: In green (mc 0), what I term the “Academe,” where graduates of the highest of three levels of the civil service examinations clustered together in an arch that offered direct access to high-ranking office both in the provinces (P173, Provincial Governor, *xunfu* 巡撫, 2a) and in the capital (P215, Right Vice Minister of Rites, Libu Yousilang 禮部右侍郎,  2a; the Ministry of Rights was reserved for examination graduates, see below). A further cluster can be seen in the grey arch opposite the lower curve (modularity class 21). These are entirely Manchu positions (not included in the Han-only version of “Examination”).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-43-*"] -->
### Realism: The Case of Prefects¶
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"c6fk9": [{"id": "14298532/LC5FSDKM", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In network terms, the above explorations are “graph-global” questions, pertaining to properties of single nodes in relation to the entire graph. More comparisons are possible if we turn to what would be termed “graph-local” questions in network terms, that is, investigation of properties that are calculated based on a neighborhood of each node (<cite id="c6fk9"><a href="#zotero%7C14298532%2FLC5FSDKM">(Needham &#38; Hodler, 2019a)</a></cite>, 6). Here, we attempt only two. First, we could show how faithfully the promotion rules in the game mimic the statutory promotion rules in “Examination”. Secondly, we will turn to the dice values which accompany the promotions in the game to gauge the value judgement of the game designer. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
For the first question, we examine the case of prefect as an example, comprising two positions in the game:  P117, Prefect in a busy prefecture (*fanfu* 煩府) and P118 Prefect in a simple prefecture (*jianfu* 簡府). This has two reasons. First, the prefect has a relatively high centrality in the game (see Gephi analysis and graph, both are in modularity class 20). Secondly, there has been a scholarly debate about the prefects lately. The debate is relevant for our argument because it shows that, while the game certainly does not reflect reality, the statutory system of the Qing, for which the “Examination of Rank-Classes” stand as proxies, did not perform much better. It was by itself a “utopia of rules.” Reality on the ground looked very differently.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"mf3z6": [{"id": "14298532/B5NTRW96", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In the Qing administrative system, the prefecture is a unit of territorial administration that is between the county and the province. A prefecture has several counties, and a province has several prefectures. Appointments to prefect positions were the subject of a recent study by Hu Heng et al. which is part of the growing body of research that is being produced out of the Chinese Government Employee Database-Qing (CGED-Q, <cite id="mf3z6"><a href="#zotero%7C14298532%2FB5NTRW96">(Hu Heng 胡恒 et al., 2020)</a></cite>). Hu Heng et al. focus on appointment procedures in the appointments of 3,403 prefects in CGED-Q (1833-1911). Prefectures had designations of importance, namely as “most important” (*zuiyao* 最要), “important” (*yao* 要), and “simple” (*jian* 簡). They also had designations of appointment prerogative, namely: 1. appointment by imperial edict (*qingzhi que* 請旨缺, 48.3% of vacancies); 2. appointment upon request of the governor (*tidiao que* 題調缺, 26.1.% of vacancies); 3. appointment by Board of Personnel (*buxuan que* 部選缺, 25.6% of vacancies). This makes prefectures a perfect case to discuss the balance of power between the court, the Ministry of Personnel, and the provincial governors. Hu argues (p. 368) that 43.3% of all vacancies (102) were to be appointed by imperial edict (*qingzhi que* 請旨缺), and these were located in the most important, connected and wealthy places. This shows that the throne maintained centralized power over the appointment process, while the Board of Personnel was comparatively weak, finding its appointments infringed by both the throne and the governors.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"6tu2u": [{"id": "14298532/G9J8Z9FU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Wu Yue, one of the most exacting scholars of Qing institutional history, subsequently attacked these findings. He argued that the official directories were highly inaccurate and hence unreliable. More often than not, they reflect an abstract appointment to a rank with no guarantee that the candidate actually showed up on the ground (as he shows in detail, some never served in the position they were nominally appointed to). Wu also dampens the idea of a power struggle in the appointment designations. The appointment procedures were highly regulated, namely by the “Examination of Rank-Classes”. The only ways for the governors to break away from these procedures were those not expressed in the official directories, namely sending appointed prefects on commissions and temporary substitutions elsewhere, while filling the vacant posts with their own substitutes (<cite id="6tu2u"><a href="#zotero%7C14298532%2FG9J8Z9FU">(Wu Yue 伍躍, 2022)</a></cite>).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
We could argue that a board game is fictional, because it does not represent the murky waters of provincial dealings. However, as Wu Yue has shown, the administrative laws of the empire did not perform more faithfully. Therefore, we feel confident that the comparison between the “Examination of Rank-Classes” and Mandarin Promotions can yield meaningful results, without caring too much about its relationship with bureaucratic reality on the ground. What we want to know is if the game replicates the “Examination” and which edition it was based on.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
For this purpose, we examined who could be appointed to prefect in the game and found that the appointments in the game are consistent with the appointments in the 1768 edition of the “Examination,” except in a few cases that can easily be explained. The classifications of prefectures into degrees of importance (see above) were not listed in the “Examination” (its sources were in other regulations). *Mandarin Promotions*, on the other hand, expresses them in a simplified way by distinguishing only between “busy (i.e. lucrative) prefecture” (*fanfu* 煩府, P117) vs. “simple prefecture” (*jianfu* 簡府, P118). This division is the same as for counties mentioned above. [Table 3](#table-32-*) below lists all positions from which appointment  to prefect is possible in both works, including both “busy” and “simple prefecture” for *Mandarin Promotions*.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"u5vvo": [{"id": "14298532/53JV9T85", "source": "zotero"}]}} editable=true jdh={"module": "object", "object": {"source": ["Appointments to Prefect in \u201cExaminations\u201d and Mandarin Promotions"], "type": "image"}} slideshow={"slide_type": ""} tags=["table-32-*"] -->
|Examination of Rank-Classes (<cite id="u5vvo"><a href="#zotero%7C14298532%2F53JV9T85">(A Gui 阿桂, 2000)</a></cite>) |Mandarin Promotions|Translation (Explanation)
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
In [Table 3](#table-32-*) we see that in some cases “Examination” is more specific, for example in C20-P129 where it distinguishes between two different capitals, the actual capital Beijing (Shuntian prefecture) and the Manchu capital Shengjing, todays Shenyang (Fengtian). In other cases, there is a lacuna in “Examination.” C48 and C51 are Manchu institutions where positions are reserved for Manchu officials, hence they are missing in the Han-only “Examination” table used for this comparison. Often, *Mandarin Promotions* is much more detailed, as in the Ministries. More on those below.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"ht5ad": [{"id": "14298532/IBITMVRZ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The most interesting difference is in the existence of the independent ting department (as opposed to Zhou-department). “Independent” means that the department (a sort of county) is not governed by a country magistrate (*zhixian* 知縣, rank-class 7a). The governing official of an independent department (*zhilizhou* 直隸州) is a department magistrate (*zhizhou* 知州, rank-class 5a), which is three classes (*ji*) higher than a magistrate, and he directly answers the governor of a province, not a prefect. The ting was a peculiar administrative unit where a prefect sent one of his two vice-prefects (*tongzhi* 同知 or *tongpan* 通判) to take direct control of an area which was often located at strategically important border regions and ruled by local tribes. Hu Heng has shown that the institutionalization of the ting did not happen before the mid eighteenth century and was due to the Qianlong’s decision in 1741 to never again increase the number of statutory officials to save government expenditures. The ossification of the imperial bureaucracy then mostly forestalled further administrative expansion and resulted in the non-conventional use of auxiliary officials for functions previously reserved to seal-holding officials, namely taxation and law. The Collected Statutes reflected the change with a time lag, and the ting officials (*zhiliting tongzhi* 直隸廳同知, *zhiliting tongpan* 直隸廳通判) first showed up in the 1822 edition (<cite id="ht5ad"><a href="#zotero%7C14298532%2FIBITMVRZ">(Hu Heng 胡恒, 2013)</a></cite>). However, even though the ting was mentioned in other parts of the expansive collection, it was never included in the “Examination” chapters (even in the 1886 edition). This shows that our version of Mandarin Promotions was designed in the early 19th century, that is, the date of 1840 on the preface of the earliest known version of this particular civil-official game board was the genuine date of creation. It also shows that the designer used the full extent of the Collected Statutes instead of simply gamifying the “Examination” table.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"l4m9j": [{"id": "14298532/B5NTRW96", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
What did prefect appointments really look like on the ground? Hu Heng et al have produced a statistics of 2,471 prefects for whom the previous position is known (<cite id="l4m9j"><a href="#zotero%7C14298532%2FB5NTRW96">(Hu Heng 胡恒 et al., 2020)</a></cite>, 381-382). If we rearrange the table a little, the breakdown looks like [Figure 7](#figure-prefect-origins-*).
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
In [Figure 7](#figure-prefect-origins-*), we find two differences from the regulations listed above. Among unexpected candidates for prefects were, firstly, those that we have termed the “Academe” and the “Censorate.” These were positions reserved for graduates of the civil service examinations. Together, they received at least 24% of all appointments.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"ac9yb": [{"id": "14298532/S78TH7KN", "source": "zotero"}], "aylay": [{"id": "14298532/3D8I6ICQ", "source": "zotero"}], "bv0nf": [{"id": "14298532/C8W4N2VE", "source": "zotero"}], "co4wq": [{"id": "14298532/VN5J5J4V", "source": "zotero"}], "f9jma": [{"id": "14298532/JJL4PW6R", "source": "zotero"}], "hcacm": [{"id": "14298532/WSGVR2JV", "source": "zotero"}], "qh8zw": [{"id": "14298532/G9J8Z9FU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The Investigating Censor (rank-class 5b) was a pivotal position, and, hence, has a high centrality in the “Examination” of 1768 (Figure 2). According to Wu Yue, the promotion path of censors changed only in 1843, in one of the few major revisions in the “Examination” chapters (<cite id="qh8zw"><a href="#zotero%7C14298532%2FG9J8Z9FU">(Wu Yue 伍躍, 2022)</a></cite>, 37-39. This revision was published as part of the Regulations of the Ministry of Personnel. <cite id="f9jma"><a href="#zotero%7C14298532%2FJJL4PW6R">(Libu, 1969)</a></cite>), Facsimile of the 1843 edition). Before this change, the Investigating Censor (rank-class 5b) could be appointed Circuit Intendant (4a), which was a major promotion in rank-class. After this change, the Investigating Censor could only be promoted to Prefect (4b), which appears as a depreciation in rank, but offered more opportunities for provincial appointment, because there were more prefectural positions. Since the throne, as we have seen above, had a say in the appointment process, appointing examination graduates from the metropolitan Academe and Censorate, provided one of the rare channels of mobility between the metropolitan and provincial bureaucracies, and gave some career advantage to examination graduates (“regular path”) against purchasers (“irregular path”). Peng Peng’s statistics (<cite id="aylay"><a href="#zotero%7C14298532%2F3D8I6ICQ">(Peng, 2022)</a></cite>, 154-155), although incomplete for the nineteenth century, corroborate this impression. They show that in relative terms the ratio of purchasers in prefects did not rise, although it did rise in the population of county magistrates as Kondo and Marsh had shown previously (<cite id="co4wq"><a href="#zotero%7C14298532%2FVN5J5J4V">(Marsh, 1962)</a></cite>; <cite id="bv0nf"><a href="#zotero%7C14298532%2FC8W4N2VE">(Kondō Hideki 近藤秀樹, 1963)</a></cite>; <cite id="ac9yb"><a href="#zotero%7C14298532%2FS78TH7KN">(Kondō, 1963)</a></cite>; <cite id="hcacm"><a href="#zotero%7C14298532%2FWSGVR2JV">(Kondō, 1963b)</a></cite>).
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"blgtc": [{"id": "14298532/6GCT89TP", "source": "zotero"}], "n2oib": [{"id": "14298532/G9J8Z9FU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The second unexpected candidate for prefect was the county magistrates (*zhixian* 知縣, 7a). Wu Yue has criticized the study by Hu Heng et al., because his statistic lists the appointment of 135 county magistrates (*zhixian*) to prefect positions. Since their rank is 7a, the promotion would jump 5 steps in the ladder of rank-classes, to be appointed prefect (4b). This was impossible. The only way to circumvent the regulations in the “Examination of Rank-classes” would have been a special edict (i.e. extraordinary imperial patronage) or perhaps purchase (<cite id="n2oib"><a href="#zotero%7C14298532%2FG9J8Z9FU">(Wu Yue 伍躍, 2022)</a></cite>, 37-47). On the other hand, in writing the biography of Li Hu 李湖 (1715- 1785), Kent Guy also claimed that a county magistrate could be directly appointed as prefect (<cite id="blgtc"><a href="#zotero%7C14298532%2F6GCT89TP">(Guy, 2014)</a></cite>, 81). How would the game behave?
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"7yhuw": [{"id": "14298532/J5HSXH8H", "source": "zotero"}], "mcbn9": [{"id": "14298532/J5HSXH8H", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We have already seen that Mandarin Promotions follows the “Examination of Rank-Classes” and did not allow a direct career move from county magistrate to prefect. Plotting Mandarin Promotions as a network graph allows us to examine longer paths. The game also simulates the results of triennial performance reviews called Great Reckoning (*daji* 大計, <cite id="7yhuw"><a href="#zotero%7C14298532%2FJ5HSXH8H">(Hucker, 1985)</a></cite>, no. 5891) in the provinces and Capital Evaluation (*jingcha* 京察, <cite id="mcbn9"><a href="#zotero%7C14298532%2FJ5HSXH8H">(Hucker, 1985)</a></cite>, no. 1189). [Table 4](#table-33-*) shows that in Mandarin Promotions the only way to be promoted from county magistrate to prefect within two rounds of dice, i.e. not going through another ranked position, was through an outstanding performance review judged as either “*zhuoyi* 卓異” (outstanding) or “*nei jiming* 內記名” (royal nomination).
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["County Magistrate to Prefect in Mandarin Promotions"]}} slideshow={"slide_type": ""} tags=["table-33-*"] -->
|County Magistrate|Great Reckoning verdict|Appointed to
|-|-|-
|C15-縣 : P92-京縣 County Magistrate in the Capital Prefecture|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a busy prefecture
|C15-縣 : P93-煩縣 County Magistrate in a difficult county|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a busy prefecture
|C15-縣 : P94-簡縣 County Magistrate in a simple county|卓異 Outstanding<br/>內記名 royal nomination|煩府 Prefect in a busy prefecture



<!-- #endregion -->

<!-- #region citation-manager={"citations": {"16wzh": [{"id": "14298532/6GCT89TP", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
In other words, the game behaves exactly as Wu Yue would have predicted. In order to be appointed prefect, a magistrate would need a special imperial edict or to purchase the higher rank. There was no regular promotion from magistrate to prefect. As a matter of fact, Kent Guy writes about Li Hu, whose biography he studied: “When the post of prefect of Tai'an became vacant, the fact was reported to the emperor who then chose the new appointee from among the officials known to him” (<cite id="16wzh"><a href="#zotero%7C14298532%2F6GCT89TP">(Guy, 2014)</a></cite>, 81). This almost exactly describes the procedure which the game refers to as “royal nomination.” Following an outstanding review (or with sufficient patronage), an official could be added to a list of nominees from which the emperor would choose for extraordinary promotion, i.e. promotions that broke the confines of the “Examination of Rank-Classes.” There was no direct and automatic promotion from county magistrate to prefect. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In addition, the rules of the game also allowed for a purchase, an option about which we know was also available in real life. In the game, the price is 5 chips per rank-class (*ji*). The county magistrate is ranked 7a, but 6a if the county is located in the capital prefecture, making five respectively three rank-classes to prefect (4b), costing 25 respectively 15 chips, up to a quarter of the initial wager at the beginning of the game.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
So, what does the case of prefect tell us about the game Mandarin Promotions? As a reminder, we study a post-1870s version of the game which is based on the 1840 original. First, the game is faithful to the statutory regulations of official promotion charts to a surprising degree, notwithstanding necessary abstraction in the performance review process. Secondly, the regulations that the game is based on are those before 1843. Thirdly, the post-1870s version did not revise the original setup to make it closer to current practice. This means that, because the game design did not change with the times, its level of abstraction increased, not because the game became more abstract, but because reality moved away. The same, though, as we have seen above, can be said for many of the Qing regulations themselves. As Wu Yue has shown, the statutory regulations themselves are not necessarily more “true” when it comes to the situation on the ground. Regulations create their own “utopia of rules.” What was in the regulations and what happened on the ground were two different things. The game mimicked the regulations. Players during the Qing dynasty must have known this, including the fact that the game remained frozen in time and was therefore increasingly outdated. But this, too, happened to the Collected Statutes. For example, the ting department, albeit securely institutionalized, was not included in the “Examination of Rank-Classes” even by the 1899 edition, the last before the Qing empire collapsed.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Value: The Case of Ministries¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
As we have argued above, all designations listed on the game chart do exist in the bureaucratic regulations of the Qing. However, nowhere in the same combination. We can use this fact to gauge the perception of the game designer. How can deviations from the regulations inform us about his value system?
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
One example is the distribution of the Six Ministries in Beijing. They are Public Works (C32), Punishments (C33), War (C34), Rites (C35), Revenue (C36), and Personnel (C37), and all have similar positions, namely:
- *Shangshu* 尚書, 1b, Minister
- *Zuo Shilang* 左侍郎, 2a, Left Vice Minister
- *You Shilang* 右侍郎, 2a, Right Vice Minister
- *Langzhong* 郎中, 5a, Department Director
- *Yuanwailang* 員外郎, 5b, Vice Department Director
- *Zhushi* 主事, 6a, Secretary

The “Examination” chapters distinguish only between the Ministry of Personnel and the rest, and treat most promotions equally, not specific to the ministry, except that the Ministry of Rites was reserved for candidates with examination degrees. Hence, it is easy to calculate the centrality of certain positions. We find that the vice department director is the position with the highest betweenness centrality (see [Game Rules: Plotting Mandarin Promotions](#anchor-subsection-42-*)).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In *Mandarin Promotions*, each ministry is listed with its full list of positions. In general, Beijing positions are overrepresented and more differentiated. Due to their duplication across ministries, we cannot determine the centrality of certain official ranks in general. For instance, we cannot say if the vice department director has the same centrality in the game as in “Examination”, because in the former that position exists in more than one ministry. However, we can determine whether the game designer assigned special interest to certain ministries and certain positions.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
For this, we again turn to a graph-local question and use the in-degree of the three lower-ranking positions in each ministry. We remind the reader that the game designer has attached value to dice rolls by naming them, namely: VIRTUE (44), TALENT (66), EFFORT (55), MEDIOCRE (33), WEAK (22), CORRUPT (11). We argue that these names are meaningful and imbue the result of the dice roll with moral value. In a way, they return meritocratic (hence competitive, agon) value to the game, which is entirely a game of luck (alea). We can, therefore, assign a “merit score” by calculating the in-degree by edge type. Merit scores by in-degree for the six ministries are in [Table 5](#table-341-*):
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Merit scores by in-degree for the six ministries"]}} slideshow={"slide_type": ""} tags=["table-341-*"] -->
Merit|War|Works|Revenue|Rites|Punishments|Personnel|
-|-|-|-|-|-|-|
VIRTUE|66|51|78|79|79|59
TALENT|49|58|76|51|73|49
EFFORT|53|54|63|52|66|70
MEDIOCRE|60|59|72|45|51|48
WEAK|42|58|64|51|45|53
CORRUPT|12|15|14|23|11|14
Total In-degree|282|295|367|301|325|293


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-34-*"] -->
On the surface, the distribution of merit scores between the six ministries appears evenly distributed with a slightly higher number of incoming edges in the Ministries of Revenue and Punishments. That there are fewer candidates appointed with a corrupt verdict is natural. Firstly, there are fewer “corrupt” scores in the entire graph. Among the MERIT relationships, 3,687 are for VIRTUE, 3,868 TALENT, 3,404 EFFORT 3,139 MEDIOCRE, 2,861 WEAK, and only 1,064 CORRUPT. The general sentiment of the game, it appears, is one of optimism. Secondly, if a “corrupt” score lands you on a position, this is mostly a demotion, i.e. a downgrading from higher rank. While virtue, talent, and effort should equally lead to success, the bias is also tilted towards virtue and talent, with the Ministries of Revenue, Punishment and Rites all strong in virtue, but only the former two are also strong in talent.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
This trend is more pronounced for the three entry-level positions in the ministries, i.e. those positions that could be directly purchased (see [Realism: The Case of Prefects](anchor-subsection-43-*)). Merit scores for entry-level positions in the six ministries are distributed as shown in [Table 6](#table-342-*):
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Merit Score for Entry Level Positions"]}} slideshow={"slide_type": ""} tags=["table-342-*"] -->
||郎中, 5a, Department Director|員外郎, 5b, Vice Department Director|主事, 6a, Secretary|Totals
-|-|-|-|-
C32-Works|P193|P194|P195||
EFFORT|4|19|11
VIRTUE|4|19|4
TALENT|4|31|13
WEAK|4|18|16
MEDIOCRE|6|16|13
CORRUPT|3|3|6
Total In-degree|25|106|63|194
|||||
C33-Punishments|P201|P202|P203
EFFORT|8|22|12
VIRTUE|6|26|14
TALENT|10|28|14
WEAK|4|10|9
MEDIOCRE|5|12|8
CORRUPT|1|4|5
Total In-degree|34|102|62|198
|
C34-War|P209|P210|P211
EFFORT|11|14|5
VIRTUE|11|12|5
TALENT|11|8|6
WEAK|6|7|5
MEDIOCRE|10|8|7
CORRUPT|1|3|5
Total In-degree|50|52|33|135
|
C35-Rites|P216|P217|P218
EFFORT|8|10|17
VIRTUE|14|9|9
TALENT|14|8|10
WEAK|8|3|17
MEDIOCRE|7|4|11
CORRUPT|4|3|6
Total In-degree|55|37|70|162
|
C36-Revenue|P226|P227|P228
EFFORT|10|17|22
VIRTUE|11|15|14
TALENT|10|16|33
WEAK|8|13|22
MEDIOCRE|7|8|21
CORRUPT|2|2|5
Total In-degree|48|71|117|236
|
C37-Personnel|P234|P235|P236
EFFORT|8|18|14
VIRTUE|13|14|10
TALENT|12|15|10
WEAK|5|9|12
MEDIOCRE|5|6|12
CORRUPT|1|4|3
Total In-degree|44|66|61|171


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
They can better be visualized in a radar chart as in [Figure 8](#figure-342-*):
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

<!-- #region citation-manager={"citations": {"p3alt": [{"id": "14298532/PX4XEZRW", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The Ministries of Revenue, Punishments and Works stand out with a greater number of incoming edges and bias towards talent. Since positions listed here were those accessible by purchase, it would not be far-fetched to conclude that the three ministries were popular among office purchasers. The balancing between virtue and talent is not self-explanatory. There has been in China a longstanding debate about whether virtue or talent was more important for official appointments. The reason was that the old examinations with their heavy emphasis on the Confucian classics (virtue) were not geared towards solving real-world problems. The debate won new urgency in the mid-nineteenth century when office selling proliferated, while socio-economic, environmental and geopolitical crises created new challenges. Defenders of office selling argued that to open this path could attract practical talent. One example comes from Wang Kaiyun 王闓運 (1833-1916): “Men who obtain office by purchase are one third less than those who obtain office by recommendation for military merit, but their talents and administrative abilities are often better than those of magistrates with regular qualification (*zhengtu*). Therefore, though it is true that office purchase is harmful to politics, the allegation that it is responsible for spoiling bureaucratic ranks is not necessarily true.” (See: <cite id="p3alt"><a href="#zotero%7C14298532%2FPX4XEZRW">(Wang, 1983)</a></cite>, 165). The game designer’s “hidden” bias seems to side with such arguments. This may also be expressed in the lower “popularity” (and tilt towards WEAK) of the Ministry of Rites, the old refuge of examination graduates.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
These three tests are limited in scope, but readers can feel free to make more tests using the data. In summary, they show that, first, *Mandarin Promotions* can be used to teach the actual operation of the Qing bureaucracy, albeit only the statutory one. Secondly, we can also confidently use the game to understand how the game designer (or game designers, as there were additions in later versions) perceived the Qing bureaucracy of his (their) time. We will turn, in the next section, [Equal opportunity?](#anchor-section-5-*), to the question of how the game perceived the idea of meritocracy and equal opportunity, which has been thought of as a guiding principle of the Qing bureaucracy since it first became known in Europe during the seventeenth century.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-5-*"] -->
## Equal opportunity? Do all players have a chance to win?¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### *Chushen*
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"nfvj4": [{"id": "14298532/F8METVWQ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
*Chushen* is a term hard to translate. It is most commonly used as a generic name for success in the civil service examinations. In this sense, it means “credentials.” However, in the Qing dynasty, the term denominated a much more diversified array of backgrounds. Having *chushen* marks the exit from commoner status and eligibility for official status. Only with *chushen*, one becomes qualified to climb up the ladder of official ranks. The status connotation of “*chushen*” may be one of the reasons that the term could have been revived by Mao Zedong in the 1950s to denote hereditary class background (See: <cite id="nfvj4"><a href="#zotero%7C14298532%2FF8METVWQ">(Xu, 2021)</a></cite>).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In *Mandarin Promotions*, commoners remain “outside the game” (*juwai* 局外, a term still used to describe outsiders in general), until fortune (the initial roll of dice) gives them chushen credentials. As one poem put it: “There are only favorites at the game table, and no commoners among our companions.” (Lanxiu Gezhu 蘭修閣主, 1873) Literally, favorites are “red guests”  (*hongke* 紅客), commoners are “white males” (*baiding* 白丁), playing at the red and white contrast of the dice and the fact that commoners did not wear official gown (white also means “plain”). Official rank, divided into 19 rank-classes, denominated eligibility for occupying a certain position, the right to wear a certain gown, and a place in the overall hierarchy of enfranchised notables.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"wu8um": [{"id": "14298532/J8BBF2K4", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Fifteen of the chushen positions are in a department on the gameboard itself labelled “*chushen* 出身” (C1). Each of these fifteen denominations does have significance in the real world of the Qing dynasty. Other (real-world) chushen categories are in other departments of the game chart. Examination degrees beyond the first degree (P10, *shengyuan* 生員), so-called “*kejia chushen* 科甲出身” are located in the departments for the provincial and metropolitan examinations. Hereditary titles of lower nobility listed below (C2) also conferred *chushen*, without being located in the “*Chushen*” department. Following the Taiping Rebellion (1850-1864) when so many officials perished in office, such titles were given to a son as a reward (<cite id="wu8um"><a href="#zotero%7C14298532%2FJ8BBF2K4">(Meyer-Fong, 2013)</a></cite>). In the game they represent a big win. [Table 7](#table-41-*) lists the chushen positions in the game:
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Chushen Provenances"]}} slideshow={"slide_type": ""} tags=["table-41-*"] -->
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
Confining ourselves to the fifteen positions in the “*Chushen*” department alone, we can for analytical purposes distinguish roughly five types of provenances: examinations, heredity, patronage (including imperial grace), incipient professionalism, and finally purchase. The game designer added value judgement by attaching dice value to each of the positions. The game is played with four dice. Dice values are abbreviated as D “double”, T “triple.” Triples are only recognized for the very first roll of dice which establishes *chushen*. Hereditary privilege catapults the player into office right away, hence it is attached to LUCK dice (see [Playing Mandarin Promotions](#anchor-subsection-32-*)). The worst dice (D1, corrupt) is the student (P15) who is trying to pass the notoriously difficult examinations for his first degree (which is attainable by the most beneficial dice value D4, styled “virtue”). Incipient professionalism (lowly clerks and the astronomers-doctors) is also bad. However, did these starting positions still have the equal chances to get ahead in the game? It is a game, after all, which is only fun if it has an equal playing field, literally. This section will use a Monte Carlo simulation to find out. Before discussing the technical details of this, we will first introduce another aspect of the game that has the potential to drastically change the role of the *chushen*, namely the possibility to purchase official rank.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-52-*"] -->
### Purchase
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"j0uwt": [{"id": "14298532/IJAXKZ39", "source": "zotero"}], "q8ntg": [{"id": "14298532/DLXZH9IP", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["anchor-section-4-*"] -->
In the life-world of the game designer, the legal sale of official rank and appointments was rampant. The institution goes back to the beginnings of the Chinese empire and certainly to the beginning of the Qing dynasty (<cite id="j0uwt"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>). However, during the latter half of the eighteenth century, the Qianlong emperor (r. 1736-1796) frowned upon the practice and rarely licensed office-selling campaigns. This changed after 1798. In the early nineteenth-century, office selling became a regular experience (<cite id="q8ntg"><a href="#zotero%7C14298532%2FDLXZH9IP">(Kaske, 2018)</a></cite>). The design of the 1840 version of Mandarin Promotions began to reflect this change and introduced office purchase as a new option.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"fkvsm": [{"id": "14298532/IJAXKZ39", "source": "zotero"}], "uk0sa": [{"id": "14298532/V8FFRKCS", "source": "zotero"}], "v3i4q": [{"id": "14298532/ZH6Y34YM", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Office purchase is the only element that returns agency to this game which was otherwise entirely determined by chance. The written rules printed in the center of the 1840 Oxford board allow office purchase up to a certain rank, at a price of 5 chips per rank-class. The rank-limit (4a in the provinces and 5a in Beijing) fully complies to the laws governing legal office selling at the time. Modern recreations of the game in Hong Kong discourage or ban office selling, because it destroys the suspense of the game (Puk Wing Kin, the historian, encourages his readers to ban office purchase, even though he faithfully explains the original rules that allow it (<cite id="uk0sa"><a href="#zotero%7C14298532%2FV8FFRKCS">(Puk Wing Kin 卜永堅, 2011)</a></cite>, p. 28). Pan Guosen who has made major changes to the game follows the Oxford chart and eliminates the 捐班候補 block (<cite id="v3i4q"><a href="#zotero%7C14298532%2FZH6Y34YM">(Pan, 2017)</a></cite>, 87-88). He still allows purchasing a reinstatement into a previous office (juanfu 捐復) after a penalty dismissal (Ibid., p. 97)). However, for historians, the expansion of office purchase in the nineteenth century raises the question whether this move increased or lowered social mobility (<cite id="fkvsm"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>, passim, argues that office purchase served to solidify status within extended lineages rather than fostering social mobility). For the game, the important question then is how the game designers viewed this question, that is, what impact does purchase have on the relative advantages of the different *chushen* positions?
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
Late nineteenth-century game boards also created a new category of “Expectant officials by purchase”, C14 in our data model, a sort of holding for office purchasers before they were appointed, then again by dice, to full positions ([Figure 9](#figure-4.2-*), see also [Figure 1](figure-game-chart-*) for its position on the game chart).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The list of offices for sale is telling. These positions were most coveted. We have the three ministerial executive positions in Beijing discussed in [Realism: The Case of Prefects](#anchor-subsection-43-*), as well as so-called “seal-holding” (*zhengyin* 正印) positions in the province which had a treasury.
- Langzhong 郎中, 5a, Department Director 
- Yuanwailang 員外郎, 5b, Vice Department Director
- Zhushi 主事, 6a, Secretary
In addition, there are four positions in the provincial bureaucracy:
- Dao 道, 4a, Circuit Intendant
- Zhifu 知府, 4b, Prefect
- Zhizhou 知州, 5b, Department Magistrate
- Zhixian 知縣, 7a, County Magistrate

There are two more categories in which all non-seal-holding offices are lumped together as one category (auxiliaries and miscellaneous officials, *zuoza* 佐雜). The category “Probation and internship” (*shiyong xuexi* 試用學習) is a further waiting category accessed by unfavorable dice from the other expectant officials.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"dp1gd": [{"id": "14298532/B5NTRW96", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-42-*"] -->
The introduction of the holding category again mirrors reality where many office purchasers spent years or decades as expectant officials without getting an appointment. In Qing office selling, what was sold was official rank with eligibility to appointment, but not the position itself. Hu Heng cites a case of a certain Wang Buduan 汪步端 who was appointed prefect in 1906 at age 52. He had purchased the Imperial Academy Collegian (P11 *jiansheng* 監生) and the rank of deputy prefect (P119 *tongzhi* 同知, 5a) in 1864, at the age of 10. This is a non-seal-holding rank and therefore cheaper. In 1903, he again purchased a rank elevation to prefect, a seal-holding position, and a peacock-feather plume decoration (P413 *hualing* 花翎). In the meantime, he had served as expectant official in various temporary commissions, before he was finally recommended (C1-P5 *baoju* 保舉) and appointed to a vacancy after 42 years (Cited from: <cite id="dp1gd"><a href="#zotero%7C14298532%2FB5NTRW96">(Hu Heng 胡恒 et al., 2020)</a></cite>, 382-383).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In game terms, on the other hand, introducing the holding category functioned as a limitation on office purchase. It gave a choice of attractive positions, but then let the players continue by dice. For the ministries, the choice made by the later game designer confirms the popularity ranking which we observed in [Realism: The Case of Prefects](#anchor-subsection-43-*): VIRTUE leads to the Ministry of Revenue, TALENT to the Ministry of Punishments, EFFORT to the Ministry of Public Works.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"beume": [{"id": "14298532/IJAXKZ39", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Our simulation will try to determine under which circumstances purchase of one of the positions among the “Expectant officials by purchase” would be beneficial, considering both the purchase price, set in the game as 5 chips per rank-class, and the resulting winning opportunities in terms of money received from the pool and other players. As we have seen in the example of Wang Budan above, purchase of office in the real world happened in several steps (for more details, see <cite id="beume"><a href="#zotero%7C14298532%2FIJAXKZ39">(Zhang, 2023)</a></cite>). In principle, the player has the free choice to purchase at any stage of the game, as long as the target office is ranked higher than the position that is currently being held by the player. However, as we shall see below when discussing the results of the simulation, among competing players, it is beneficial to purchase an office very early on, often directly from the starting position.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Since the overt game rules are incomplete, we had to introduce a few rules of our own in order to limit the number of possible scenarios. To maintain plausibility from the perspective of an informed nineteenth-century Chinese player, we tried to shape these rules based on our understanding of real-world office selling.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Firstly, special rules apply to P8 (Student of Astronomy) and P9 (Student of Medicine). As we have already stated above, they are forced to purchase instantly to bail out from their provenance. Once they have moved on from their starting position in their respective careers as astronomer or physician, game rules exclude them from further purchase.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"63p0s": [{"id": "14298532/SLU49A89", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Secondly, in the real Qing world, all office purchasers had to purchase the degree of Imperial Academy Collegian first. Therefore, we added a price for an Imperial Academy Collegian (C1-出身 : P11-監生) of 5 chips, that has to be purchased first by players wanting to purchase in the next step one of the positions from the “Expectant officials by purchase” ([Figure 9](#figure-4.2-*)), unless they happen to already hold that position or any ranked position by dice roll. Dice rules, written in small script under each header, treat P11 the same as the Licentiate (C1-出身 : P10-生員). They assume that he would continue towards higher examination glory. In our rules, if a player comes to P11 by dice or by purchase, he has the free choice whether to proceed according to dice rules, which stipulate continuing to the provincial examinations, or to purchase a position from the list in C14. The Licentiate P10, by contrast, has to purchase P11 before he is allowed to purchase office instead of embarking on the examination path, but he can get a discount (2 chips). This rule is also informed by real-world practice, where the purchase of P11 often served to skip some initial competitive steps in the three-step imperial examinations (<cite id="63p0s"><a href="#zotero%7C14298532%2FSLU49A89">(Wu Yue 伍跃, 2021)</a></cite>).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Thirdly, we have to clarify unclear or incomplete rules in the C14 department of office purchasers ([Figure 9](#figure-4.2-*)):
1. For the dice roll “corrupt” the rule is “stop appointment  (*tingbu* 停補)”. We interpret this rule as being sent back to Imperial Academy Collegian (C1-出身 : P11-監生).
2. There are two positions, P89 and P90, which do not refer to actual positions but to a category, namely auxiliary and miscellaneous officials (*zuoza* 佐雜) as opposed to seal-holding and executive officers. Since these positions do not offer specific targets for outbound moves, in the simulation, players can choose from a list of eligible positions of appropriate rank in either the capital or the provinces, depending on whether they come from P89 or P90. When a player moves to these positions (P89 and P90) their previous rank is stored in a special variable. In their next turn, they can make a choice among all positions that satisfy the following three criteria: 1) the target position is listed on a predefined list of purchasable auxiliary position (to exclude seal-holding positions); 2) the rank of the target position is higher than the previous rank; 3) the position is in the correct location (Beijing for P89, Provinces for P90). The price of the purchase is then calculated based on the rank of the specific position they go to in the second turn.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Technical Background: Monte Carlo and the Rules of Purchase¶
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Analysing the question of opportunities in the game, both with and without the presence of purchase, requires a technical setup that goes far beyond the network approach used in the previous section, [“Utopias of Rules”?](#anchor-section-4-*). While, as we have seen, that approach can be used to gain insight into several aspects of its design, there are also some limitations that are hard to overcome. Specifically, there are mechanisms in the game that need to take into account the precise path that a player has taken before ending up in a certain position. First, to make accurate statements about monetary aspects of the game, each transaction with the pool or in between players has to be recorded. Secondly, there are a few special rules in the game that limit access to certain positions depending on the background of the player, that is, whether or not they ever held specific positions earlier in the game. While in theory, it would be possible to account for these in a network, by defining each state as a tuple similar to the approach for concurrent nodes (see [Career paths as network and tree](#anchor-subsection-34-*)), in practice this would lead to an unacceptable blow-up in the state space.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"fbuny": [{"id": "14298532/P4MRZKFS", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Another possibility for the analysis of a game would be deriving a system of mathematical equations that give an explicit solution to the various probabilities that one might be interested in. This has been done e.g. for the *Game of the Goose* (<cite id="fbuny"><a href="#zotero%7C14298532%2FP4MRZKFS">(Groote et al., 2016)</a></cite>). However, this method is already quite involved for the much simpler *Game of the Goose* without even taking monetary aspects into account.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Hence, we have decided to pursue a straightforward yet effective approach, using a Monte Carlo method. Monte Carlo methods have been used extensively to study systems that are too complex to derive an explicit solution. They work by simulating the system for a large number of times, such that by the Law of Large Numbers, the observed distribution of outcomes will converge to their expected values.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In practical terms, in order to conduct the Monte Carlo experiment, we implemented the rules of the game (including the provisions for purchase partly made up by us) in Python, using the existing data in the CSV data files as a basis. While the regular flow of the game was relatively easy to implement from the basic rules, the simulation becomes much more difficult when also considering special rules that only apply in certain circumstances, such as a few positions being restricted to persons coming from a particular background, or the game mechanisms for astronomers and physicians that are locked into their career path unless they immediately buy out of it. Furthermore, while the course of the game is mostly decided by the roll of the dice, there are a few elements of choice, especially the option to purchase an office, for which we had to decide on and implement realistic strategies of how players would behave when they have the opportunity to influence the run of the game. These will be described in detail in [When would purchase be luctrative?](#anchor-subsection-55-*), after first discussing the issue of opportunities without purchase in the following sections.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-subsection-54-*"] -->
### Simulation Results without Purchase
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Using the implementation of the game in Python, it is easy to collect data about the properties of certain positions by having the computer repeatedly play out entire games. In each game, we record relevant events such as what (random) dice rolls the players made, to which positions they moved accordingly, and how much money they received. Since simulating the game without purchase is computationally speaking extremely easy, for the results in this section, 100,000 playthroughs with four players each were conducted. Since we are mostly interested in extrapolating from this to the expected fate of individual players, this gives 400,000 unique traces of individual playthroughs of single players.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
In the following, we want to use this data to analyze the different chushen. Since the simulation precisely follows the prescribed rules in assigning *chushen* positions according to dice rolls, in the collected data, the *chushen* positions that are associated with dice combinations that are more likely to occur (like doubles) are overrepresented, while other *chushen* (like those reached by triples) are underrepresented. Hence, to have a meaningful analysis, it is important to conduct a sufficient number of experiments so that even for unlikely starting positions there is enough data. Using the 100,000 simulations, the least visited starting position with 403 visits is notably P16, the Sacred Prince (*yanshenggong* 衍聖公), or direct descendent of Confucius, whose position is accessed by the auspicious all-equals 4, which is the luckiest dice available.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In each playthrough, all players start – just as in the game – outside the game board as prescribed in the rules. Hence, in order to analyze the different chushen, we have to group playthroughs by the position that the player first arrived at. Then, the chushen can be compared with each other by taking in-group averages for the values we are interested in, which will be described below.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
First, we consider how long it takes players starting from different *chushen* to reach the end of the game, i.e. one of the final retirement positions. [Table 8](#table-441-*) shows the average number of hops until retirement for the different chushen. The average over all playthroughs in 100,000 simulations with four players is as high as 37 (sd: 12.3), being most heavily influenced by those chushen that one can obtain with a double, i.e. P10-P15, as these are more likely to occur. Observe that in the simulation, a move corresponds to one hop in the network. This is not exactly the same as a roll of dice, as some combinations will not lead to any change in the gameboard, while for others, the player can take multiple steps at once.
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Simulation results without purchase"]}} slideshow={"slide_type": ""} tags=["table-441-*"] -->
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
[Table 8](#anchor-table-441-*) also contains a column showing average effective money. This value is calculated by adding up all the money that a player receives in a given playthrough, both from the pool and from other players, and subtracting everything he has to pay, again both to the pool and directly to other players. Looking at the data in the table, it becomes immediately clear that for most *chushen* the game is – on average – pretty close to a zero-sum game, i.e. getting one provenance over the other in the beginning does not mean that the player should expect to win or lose more or less money compared to other *chushen*. Given the zero-sum nature of the game, this is of course not entirely unexpected, since all income must be balanced out with the expenses of the other players. It is nevertheless interesting to observe that at least at the level of *chushen*, the players are mostly not destined for a path from the start that will lead to them gaining or losing a lot of money with high probability. The clearest exceptions to this are to be found in the hereditary ranks (P17-P21) which on average receive much more money from other players than they have to pay themselves. This is easily explained by the fact that they already receive a significant payout in the beginning just for the fact that they got this particular starting position. Because these provenances are so unlikely to occur compared to the regular *chushen*, they do not have a large effect on the overall expectation values of the other starting positions, i.e. in an average game, a player need not be afraid to have to pay out a lot of money to a fellow player who obtained a hereditary rank.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Among the other positions, the only *chushen* that on average have a significant positive return both in winning money from the pool as well as from other players are the two Manchu positions (P7, P12) and P6 (Special palace examination, *cike* 詞科). P1 (Honorary Licentiate, *yinsheng* 蔭生) and P4 (Imperial grace, *enshang* 恩賞) both have a negative expected return from the pool, but this is more than made up for by the significant amount of money they receive from other players.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"6bx21": [{"id": "14298532/6XCI2QWJ", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
On the other end of the spectrum, the positions that on average lose more than a trivial amount of money are those that we categorized as incipient professionalism, i.e. the clerks (P13, P14) and Students of Astronomy and Medicine (P8, P9). This seems to point to a value system that did not cherish specialized knowledge (On the clerks see: <cite id="6bx21"><a href="#zotero%7C14298532%2F6XCI2QWJ">(Kaske, 2012)</a></cite>). The latter two also had short paths and largely cul-de-sac careers within the same department (especially P9). Thus, our simulation confirms the intuition of the rule writer that suggests that players that receive one of these two *chushen* should bail out (see [Purchase](#anchor-subsection-52-*)).
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Finally, looking at the average final rank that players starting from the different chushen achieve, also shown in [Table 8](#anchor-table-441-*), we can see that there does not seem to be a large difference. The average rank transformed to our linear scale over all playthroughs is slightly above 17.5, corresponding to a rank in the traditional system of between 2a and 1b. Aside from the lucky positions, two noticeable bumps are again the two Manchu *chushen* (P7, P12). This is presumably due to their privileged access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) which is pivotal to reach P352 and thereby the highest rank-class 1a. For Non-Manchus, this privilege is only granted to those top-tier *jinshi* degree holders who went through the Hanlin Academy (C56 *Hanlinyuan* 翰林院). Players from other backgrounds are forced into early retirement when they would have reached this position, thus cutting short their chance to reach a higher final rank. To spend some time at the highest rank is advantageous also in monetary terms, because instead of a progression in rank-class, the player becomes eligible for honorific rewards including palace titles (C60 *gongxian* 宮銜) and special awards (C64 *te’en* 特恩) which come with monetary gifts. Thus, this rule also explains the favorable status of the Manchu *chushen* in monetary terms noted above.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Aside from starting positions, we can also group the data by other properties that distinguish particular backgrounds. For example, [Table 9](#table-442-*) shows the average outcomes for players who did or did not go through the examination system. For this purpose, we record during the simulation in a variable for each player whether they have visited one of the positions marked as “exam” in our database, which are spread over several departments located adjacent to the chushen positions (C3, C4, C6, C7, C8, see [Figure 1](#figure-game-chart-*) for the location). As can be seen, the most significant difference in outcomes between the players who visited one of these positions and those that did not is not in the number of moves or the achieved rank class, but in the monetary results of the game. Players who went through the examination system have a slightly positive expected return, originating mostly from payments the other players have to directly make to them.
<!-- #endregion -->

<!-- #region editable=true jdh={"module": "object", "object": {"source": ["Simulation results by examination system"]}} slideshow={"slide_type": ""} tags=["table-442-*"] -->
Did go through examination system?|Average number of hops until retirement|Average effective money (From/to pool, From/to other players)|Average final rank (1a = 19, unclassed = 1)|
-|-|-|-
Yes|36.8|5.9 (1.4, 4.5)|17.8|
No|37.3|-4.1 (-0.9, -3.1)|17.8|


<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Overall, our findings reveal that for all *chushen* positions, except the student of medicine (P9), the opportunities to get to the highest ranks are evenly spread. However, in terms of monetary reward, hereditary privilege and imperial grace trump all other provenances. Graduates of the imperial examinations also have positive returns on average, but much humbler than the hereditary group. This, again, may have been due to access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) which is pivotal to reach P352. If this is true, then only those examination candidates would benefit who reach the top-tier *jinshi* degree and were admitted to the Hanlin Academy (C56). Other *chushen* have slightly negative outcomes on average.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Overall, our findings reveal that for all *chushen* positions, except the student of medicine (P9), the opportunities to get to the highest ranks are evenly spread. However, in terms of monetary reward, hereditary privilege and imperial grace trump all other provenances. Graduates of the imperial examinations also have positive returns on average, but much humbler than the hereditary group. This, again, may have been due to access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) which is pivotal to reach P352. If this is true, then only those examination candidates would benefit who reach the top-tier *jinshi* degree and were admitted to the Hanlin Academy (C56). Other provenances have slightly negative outcomes on average.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### When would purchase be lucrative? 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In the preceding section we have analysed the role of *chushen* credentials without purchase, i.e. in a setting where the players are completely subject to the roll of dice. As we have seen, a few hard to reach, yet especially favourable *chushen* can lead to high expected outcome, contrasted with middling results for most players. In this section, we will consider the game with the additional possibility of purchase. Since this poses some technical difficulties, we will start by describing the modifications to the simulation that were necessary to make this possible.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In general, the question under which circumstances office purchase is beneficial to the player would require an extremely involved game theoretic analysis, because the strategies pursued by other players might affect the choice of whether one should buy an office or not. However, our purpose here is not to obtain an optimal strategy for playing the game. Rather, we are interested in understanding the reality of the game in a way that aligns with what the game designers and players could reasonably know about its mathematical realities. Since the next move after purchase will be determined through dice rolls and after that, potentially also the decisions of the others, players are faced with a high amount of uncertainty. Furthermore, due to the abundance of positions that can be attained after leaving the *chushen*, the same configurations of player tokens being in certain positions would hardly ever be achieved again in subsequent playthroughs, meaning that past experience is of limited use in subsequent playthroughs.
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"rc8qg": [{"id": "14298532/JQ8Q5PUU", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Hence, for the purposes of this study, we decided to implement a relatively simple artificial intelligence approach, that makes the decision of whether a position should be bought or not based on simulating a fixed number of playthroughs for each possible choice, giving a rough version of Monte Carlo Tree Search (For a similar application to a board game, see e.g. <cite id="rc8qg"><a href="#zotero%7C14298532%2FJQ8Q5PUU">(Szita et al., 2010)</a></cite>). Whenever a player has the choice to either purchase from the C14 list of “Expectant officials by purchase”, or if necessary given their *chushen*, the position Imperial Academy Collegian (P11, see [Purchase](#anchor-subsection-52-*) above) or else throw the dice, all possible options, including not purchasing office, are evaluated by copying the game state, enacting the option under consideration and then continuing the game until it reaches its end. We will play 10 times for each of the options that could be purchased, and again 10 times for the option without purchase. After finishing these playthroughs, we then select the choice that resulted in the highest average monetary gains for the player for whom the algorithm is invoked. In case the player has purchased one of the auxiliary official positions (P89 and P90) in their previous turn, and has to decide on one real position to move to in their current term, the same decision procedure is invoked to decide between the options.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
 Since our interpretation of the rules allows the players to purchase office from most positions, the other players might decide to purchase office in response to the different choices one player makes. For example, it might turn out to be beneficial to purchase office for a player *b* after player *a* has done so, in order to avoid falling behind the other players. However, considerations for potential reactions from *b* will have an impact on *a*’s decision to purchase in the first place. For example, if a purchase simply results in a stalemate because the other players can just counter it by purchasing themselves, it might not be beneficial for *a*  to purchase in the first place. In order to account for such phenomena, when executing the simulation of the purchase options described above, different choices are also simulated in a recursive manner for the other players. However, in order to stay true to the objective of not aiming towards an optimal strategy, but rather to reflect the uncertainty faced by the historic actors who participated in the game, we decided to limit the number of branches that are investigated in this way. In particular, in any simulated playthrough, at most four levels of recursive purchase decisions are evaluated, beyond which the game is simply played without purchase until the end. Furthermore, while for the initial simulation, each purchase option is evaluated ten times and the one giving the highest average chosen, for the nested simulations, each option is only evaluated once, and for those occurring in the third or fourth level of recursion, only a randomly chosen subset of options is evaluated at all.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Even given these simplifications, the decision strategy outlined above requires considerable computational power, making each playthrough take significantly more time than was the case for the simulation without purchase. Hence, the simulation with purchase was only run for 2000 playthroughs, each with four players, giving 8000 playthroughs of individual players, during which 34,781 purchase decisions were evaluated. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
As a first result,  the algorithm outlined above leads to  almost all the players purchasing office very early. In fact, in 7992 of the 8000 playthroughs of individual players, a purchase was made, on average occurring after throwing the dice 2.6 times (sd: 3.75). The decision to make a purchase instead of simply relying on dice rolls is supported quite strongly by the simulations, indicated by a high average difference between the simulated outcomes of the best purchase option and non-purchase. The average difference in monetary outcome of the ten simulations for the purchase option with the highest average outcome on the one hand, and the ten simulations for the option not to purchase on the other hand was 44.7 (sd: 32.2). However, when examining the results of the simulations closely, it becomes clear that in any case, the decision must be made under a considerable degree of uncertainty. The standard deviation of the results of the ten simulations for each option, averaged over all choices, is as high as 86.3. Given that after the purchase, the game mostly progresses by further dice throws, and potential actions by the other players which are also hard to predict, this is of course not surprising. Hence, even when including the potential of purchase, the experience of the historic players must still have been one dominated by luck and not planned decision making.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
One potential implication of allowing purchase in the rules of the game is that it might level the playing field, by giving players with an unfavorable *chushen* the chance to make up for their disadvantage. This is suggested by the rules themselves which strongly encourage Students of Astronomy and Medicine to bail out from their *chushen*. Table [10](#table-451-*), which displays the average outcomes of players by *chushen* with purchase shows that this is indeed the case. Firstly, purchase significantly reduces the number of hops until retirement for all players. Secondly, it reduces both losses and gains for most players, thus leveling the final results. There are exceptions. In comparison to Table [10](#table-441-*), showing the situation without the purchase, the average results of which are also reproduced in Table [10](#table-451-*), some positions may turn their (average) fate from negative to positive (P5, P15) or from positive to negative (P11, P12). Observe that due to the lower number of total playthroughs, the hereditary positions are not included in Table [10](#table-451-*), since they were not visited enough times to obtain reliable results. Due to their immediate gain of a significant amount of money, we expect that they would retain an advantage above other positions.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
However, according to our interpretation of the rules, the more favorable *chushen* still have a head-start by not having to purchase the Imperial Academy Collegian (P11) first, limiting the equalizing effects of purchase. P8-10 and P13-15, who share this obligation, continue to be at a financial disadvantage. Most prominently, in comparison to the simulation without purchase, the monetary results of the adopted simulation favor Manchu *chushen* (P7, P12) even more strongly than before. We can speculate that this is because the Manchu-exclusive positions feature only in late-game. As we have explained in the previous section, privileged access to the Assistant Grand Secretary (P353 *xieban daxueshi* 協辦大學士) in the late game is one of the key advantages of a Manchu *chushen*. Since the simulation with purchase leads to the early game progressing much faster than was the case without purchase, a late game advantage naturally becomes even more beneficial.

<!-- #endregion -->

```python editable=true jdh={"module": "object", "object": {"source": ["Simulation results for purchase"]}} slideshow={"slide_type": ""} tags=["table-451-*", "data-table"]
pandas.read_csv("script/Table 10_purchase_simulation_results.csv")
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
In summary, our numerical findings do confirm a tendency to speed up promotion and level the results between the different *chushen*, creating a strong incentive to purchase, especially (but not only) for players seeking to escape from an unfavourable start in the game. As soon as one player starts to purchase, other players will follow. The findings from our simulation show that in almost all games purchases were made. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
This confirms the intuition of some modern day editions of the game that discourage the use of this mechanism, because it makes the game unbalanced and, presumably, less fun.  However, as we have seen, considerable uncertainty remains even with purchase. Even if,  for certain *chushen* provenances, results are more or less favorable with purchase on average, this is far from guaranteed for the individual player.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["anchor-section-6-*"] -->
## Conclusions
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
The goal of this paper has been twofold: First, we wanted to understand what kind of bureaucratic reality the game mimics and how close it came to this reality. We also hoped to learn how the game designer understood and judged this reality. Secondly, we wanted to know how the category of *chushen* provenances, namely the initial status of entrants into the enfranchised holders of official rank (hereditary privilege, Imperial grace, examination, incipient professionalism), influenced game chances.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
In order to answer these questions, we have used two digital approaches. First, we have modelled the game as a network, and applied techniques inspired from research into transportation networks to understand the flow of personnel between the positions on the game board. Second, we have used a simulation to obtain accurate numerical values for the expected outcomes of the game both with and without the possibility of purchase. Our implementation shows the feasibility of applying digital methods to a historic board game. As we have seen, this proved to be particularly challenging because the rules of the game contain many intricate provisions to increase its realism.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
We found that the game was both a mimicry and metaphor of the statutory nineteenth-century Qing officialdom. As a didactic game, *Mandarin Promotions* mimicked the statutory regulations of rank promotions as closely as possible on a single chart, considering the necessary symmetry in the dice moves (mostly limited to six options). At the same time, the general outlook of its anonymous designer was an optimistic one, different from the original intentions of the Magie’s *Landlord Game* or the Böttger’s *Bürocratopoly* which started out as social criticism. Purchase of rank is included in this optimism as a viable and, in lived reality, completely legal option.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
At the same time, our simulation of the experiences made by players starting out from different *chushen* show that, far from the meritocratic mandarinate imagined by many China-watchers and historians since the European Enlightenment, the life chances depicted in the game were skewed towards hereditary privilege (especially the Manchus) and imperial grace. When including the choice of office purchase, this created strong incentives to seek promotion by that venue leading to pervasive venality. As the poem cited in [Can we study a historical board game as historians?](#anchor-section-2-*) said: “Good offices in fact are all up for pay.” Uncertainty and luck, on the other hand, pervaded the choices for both paths, the presumably meritocratic “regular” path and the venal “irregular” path into officialdom. Considering the popularity of the game throughout the nineteenth century, we are inclined to see this as an expression of the shared life experiences of the players, many of whom were aspiring official status themselves.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Acknowledgements
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
Elisabeth Kaske wishes to thank Puk Wing Kin and Jacob Schmidt-Madsen for very helpful remarks on a draft of this paper. Gus Chan did the initial typing of the game chart into an Excel sheet. Robin Howes is credited with the graphic overlay of our numbers on the game chart.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["bibliography", "hidden"] -->
<!-- BIBLIOGRAPHY START -->
<div class="csl-bib-body">
  <div class="csl-entry"><i id="zotero|14298532/53JV9T85"></i>A Gui 阿桂. (2000). 銓選漢官品級考四卷. In <i>欽定吏部則例 [乾隆朝] (1782)</i> (據清乾隆四十八年武英殿刻本影印, pp. 40–80). 海南出版社.</div>
  <div class="csl-entry"><i id="zotero|14298532/JVTS5CKH"></i>Batchelor, R. K. (2014). <i>London: The Selden Map and the Making of a Global City, 1549–1689</i>. University of Chicago Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/WB58FURK"></i>Blondel, V. D., Guillaume, J.-L., Lambiotte, R., &#38; Lefebvre, E. (2008). Fast unfolding of communities in large networks. <i>Journal of Statistical Mechanics: Theory and Experiment</i>, <i>2008</i>(10), 1–12. <a href="https://doi.org/10.1088/1742-5468/2008/10/P10008">https://doi.org/10.1088/1742-5468/2008/10/P10008</a></div>
  <div class="csl-entry"><i id="zotero|14298532/VIW5D949"></i>Bourdieu, P. (1990). Book I: Critique of Theoretical Reason. In <i>The Logic of Practice</i> (pp. 22–141). Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/G7UZDYUU"></i>Brunnert, H. S. (Hippolit S., &#38; Hagelstrom, V. V. (1912). <i>Present day political organization of China</i>. Book World. <a href="http://archive.org/details/presentdaypoliti00brunuoft">http://archive.org/details/presentdaypoliti00brunuoft</a></div>
  <div class="csl-entry"><i id="zotero|14298532/6SYD6Z2W"></i>Caillois, R. (2001). <i>Man, Play, and Games</i>. University of Illinois Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/8QEMK6W6"></i>Campbell, C., Lee, J., &#38; Ren, Y. 任玉雪. (2025, October 6). China Government Employee Database – Qing (CGED-Q) 中国历史官员数据库: 清代. <i>Lee-Campbell Group 李康研究團隊</i>. <a href="https://leecampbellgroup.blog/projects/china-government-employee-database-qing-cged-q/">https://leecampbellgroup.blog/projects/china-government-employee-database-qing-cged-q/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/B4HFQQLN"></i>Chen, B. (2019). <i>Origins and Career Patterns of the Qing Government Officials (1850-1912): Evidence from the China Government Employee Dataset-Qing (CGED-Q)</i> [Ph.D. dissertation]. Hong Kong University of Science and Technology.</div>
  <div class="csl-entry"><i id="zotero|14298532/XQEIL32V"></i>Chen, B., Campbell, C., Ren, Y., &#38; Lee, J. (2020). Big Data for the Study of Qing Officialdom: The China Government Employee Database-Qing (CGED-Q). <i>Journal of Chinese History</i>, <i>4</i>(2), 431–460. <a href="https://doi.org/10.1017/jch.2020.15">https://doi.org/10.1017/jch.2020.15</a></div>
  <div class="csl-entry"><i id="zotero|14298532/FVGZ3ZFN"></i>Chu Shiuon 徐兆安. (2023). The longer abolition of the Chinese imperial examination system (1900s–1910s). <i>International Journal of Asian Studies</i>, <i>20</i>(2), 721–737. <a href="https://www.cambridge.org/core/journals/international-journal-of-asian-studies/article/longer-abolition-of-the-chinese-imperial-examination-system-1900s1910s/014F0266625C85B4F567840A45018AD5">https://www.cambridge.org/core/journals/international-journal-of-asian-studies/article/longer-abolition-of-the-chinese-imperial-examination-system-1900s1910s/014F0266625C85B4F567840A45018AD5</a></div>
  <div class="csl-entry"><i id="zotero|14298532/DN3VH8TV"></i>Culin, S. (1895). <i>Chinese Games with Dice and Dominoes</i>. U.S. Government Printing Office.</div>
  <div class="csl-entry"><i id="zotero|14298532/6GTU5NGL"></i>DDR-Museum. (2018). <i>Die Geschichte Des Spiels Und Seines Erfinders Martin Böttger, Bürokratopoly</i>. <a href="https://www.buerokratopoly.de/portfolio/geschichte-des-spiel/">https://www.buerokratopoly.de/portfolio/geschichte-des-spiel/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/85FJBBY2"></i>Duindam, J. (2015). <i>Dynasties: A Global History of Power, 1300–1800</i>. Cambridge University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/CWESQSGQ"></i>Elman, B. A. (2000). <i>A Cultural History of Civil Examinations in Late Imperial China</i>. University of California Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/VKHBKXRB"></i>Elman, B. A. (2013). <i>Civil Examinations and Meritocracy in Late Imperial China</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/KAWPABR8"></i>Eubanks C. (2016). Playing at Empire: The Ludic Fantasy of Sugoroku in Early-Twentieth-Century Japan. <i>Verge: Studies in Global Asias</i>, <i>2</i>(2), 36–57. <a href="https://doi.org/10.5749/vergstudglobasia.2.2.0036">https://doi.org/10.5749/vergstudglobasia.2.2.0036</a></div>
  <div class="csl-entry"><i id="zotero|14298532/SF8BLY5P"></i>Graeber, D. (2015). <i>The Utopia of Rules: On Technology, Stupidity, and the Secret Joys of Bureaucracy</i>. Melville House.</div>
  <div class="csl-entry"><i id="zotero|14298532/P4MRZKFS"></i>Groote, J. F., Wiedijk, F., &#38; Zantema, H. (2016). A Probabilistic Analysis of the Game of the Goose. <i>SIAM Review</i>, <i>58</i>(1), 143–155.</div>
  <div class="csl-entry"><i id="zotero|14298532/C92QNES9"></i>Gu Wu Lü’eguan zhu 古吳绿萼館主. (1887, February 7). Ti Shengguantu 題陞官圖. <i>Shenbao 申報</i>.</div>
  <div class="csl-entry"><i id="zotero|14298532/6GCT89TP"></i>Guy R. K. (2014). Routine Promotions: Li Hu and the Dusty Byways of Empire. In Duindam J. &#38; Dabringhaus S. (Eds.), <i>The Dynastic Centre and the Provinces: Agents and Interactions</i> (pp. 74–93). Brill. <a href="https://opendata.uni-halle.de//handle/1981185920/110615">https://opendata.uni-halle.de//handle/1981185920/110615</a></div>
  <div class="csl-entry"><i id="zotero|14298532/RISMH8PS"></i>Harvard University, Academia Sinica, &#38; Peking University. (2025, May). <i>China Biographical Database Project (CBDB)</i>. <a href="https://projects.iq.harvard.edu/cbdb/home">https://projects.iq.harvard.edu/cbdb/home</a></div>
  <div class="csl-entry"><i id="zotero|14298532/PQVWKAP3"></i>Helliwel, D. (2014, January 10). The Promotion Chart. <i>SERICA</i>. <a href="https://serica.blog/2014/01/10/the-promotion-chart/">https://serica.blog/2014/01/10/the-promotion-chart/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/PB9GMRPC"></i>Ho, P. (1980). <i>The Ladder of Success in Imperial China: Aspects of Social Mobility, 1368-1911</i>. Columbia University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/ZLCXSS4P"></i>Hsieh, P. C. (1925). <i>The Government of China (1644-1911)</i>. Johns Hopkins Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/IBITMVRZ"></i>Hu Heng 胡恒. (2013). Tingzhi qiyuan jiqi zai Qingdai de yanbian 厅制起源及其在清代的演变. <i>Wen Shi 文史</i>, <i>2</i>, 253–287.</div>
  <div class="csl-entry"><i id="zotero|14298532/B5NTRW96"></i>Hu Heng 胡恒, Chen Bijia 陳必佳, &#38; Kang Wenlin 康文林. (2020). Qingdai zhifu xuanren de kongjian yu lianghua fenxi: zi zhengqu fendeng, Jinshenlu shujuku wei zhongxin 清代知府選任的空間與量化分析－以政區分等、《縉紳錄》數據庫為中心. <i>Xinya Xuebao 新亞學報</i>, <i>37</i>, 339–398.</div>
  <div class="csl-entry"><i id="zotero|14298532/J5HSXH8H"></i>Hucker, C. O. (1985). <i>A Dictionary of Official Titles in Imperial China</i>. Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/NSGHLJTT"></i>Huizinga, J. H. (1950). <i>Homo Ludens: A Study of the Play-element in Culture</i>. Beacon Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/BXSXXT84"></i>Hyde, T. (1694). <i>Historia Nerdiludii, hoc est dicere, Trunculorum: cum quibusdam aliis Arabum, Persarum, Indorum, Chinensium &#38; aliarum Gentium Ludis ...</i> Theatrum Sheldonianum.</div>
  <div class="csl-entry"><i id="zotero|14298532/Q3B2LDZ3"></i>Kaske, E. (2011). Fund-Raising Wars: Office Selling and Interprovincial Finance in Nineteenth-Century China. <i>Harvard Journal of Asiatic Studies</i>, <i>71</i>(1), 69–141. <a href="https://doi.org/10.1353/jas.2011.0006">https://doi.org/10.1353/jas.2011.0006</a></div>
  <div class="csl-entry"><i id="zotero|14298532/6XCI2QWJ"></i>Kaske, E. (2012). Metropolitan Clerks and Venality in Qing China: The Great 1830 Forgery Case. <i>T’oung Pao</i>, <i>98</i>(1–3), 217–269. <a href="https://doi.org/10.1163/156853212X634626">https://doi.org/10.1163/156853212X634626</a></div>
  <div class="csl-entry"><i id="zotero|14298532/DLXZH9IP"></i>Kaske, E. (2018). Austerity in times of war: government finance in early nineteenth-century China. <i>Financial History Review</i>, <i>25</i>(1), 71–96. <a href="https://doi.org/10.1017/S0968565017000300">https://doi.org/10.1017/S0968565017000300</a></div>
  <div class="csl-entry"><i id="zotero|14298532/7VKH8LPN"></i>Keliher, M. (2016). Administrative Law and the Making of the First Da Qing Huidian. <i>Late Imperial China</i>, <i>37</i>(1), 55–107. <a href="https://doi.org/10.1353/late.2016.0007">https://doi.org/10.1353/late.2016.0007</a></div>
  <div class="csl-entry"><i id="zotero|14298532/WSGVR2JV"></i>Kondō, H. 近藤秀樹. (1963a). Shindai no ennō to kanryō shakai no shūmatsu (1) 清代の捐納と官僚社会の終末-上-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(2), 82–110. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877019">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877019</a></div>
  <div class="csl-entry"><i id="zotero|14298532/S78TH7KN"></i>Kondō, H. 近藤秀樹. (1963b). Shindai no ennō to kanryō shakai no shūmatsu (2) 清代の捐納と官僚社会の終末-下-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(4), 60–85. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877036">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877036</a></div>
  <div class="csl-entry"><i id="zotero|14298532/C8W4N2VE"></i>Kondō Hideki 近藤秀樹. (1963). Shindai no ennō to kanryō shakai no shūmatsu (3) 清代の捐納と官僚社会の終末-中-. <i>Shirin 史林 (The Journal of History)</i>, <i>46</i>(3), 77–100. <a href="https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877028">https://ci-1nii-1ac-1jp-10097cb290175.erf.sbb.spk-berlin.de/naid/40001877028</a></div>
  <div class="csl-entry"><i id="zotero|14298532/QNAXB5L3"></i>Li, E. (2023). <i>Betting on the Civil Service Examinations: The Lottery in Late Qing China</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/JJL4PW6R"></i>Libu. (1969). <i>Qinding libu zeli 钦定吏部则例 [Regulations of the Ministry of Personnel]</i> (Facsimile of the 1843 edition). Chengwen chubanshe 成文出版社.</div>
  <div class="csl-entry"><i id="zotero|14298532/G7HQLMZ7"></i>Lo, A. (2004). Official Aspirations: Chinese Promotion Games. In C. Mackenzie &#38; I. Finkel (Eds.), <i>Asian Games: The Art of Contest</i> (pp. 64–75). Asia Society (USA). <a href="https://eprints.soas.ac.uk/1294/">https://eprints.soas.ac.uk/1294/</a></div>
  <div class="csl-entry"><i id="zotero|14298532/VN5J5J4V"></i>Marsh, R. M. (1962). The Venality of Provincial Office in China and in Comparative Perspective. <i>Comparative Studies in Society and History</i>, <i>4</i>(4), 454–466. JSTOR. <a href="https://www.jstor.org/stable/177694">https://www.jstor.org/stable/177694</a></div>
  <div class="csl-entry"><i id="zotero|14298532/VRXHV5XJ"></i>Metzger, T. A. (1983). <i>The Internal Organization of Ch’ing Bureaucracy: Legal, Normative, and Communication Aspects</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/J8BBF2K4"></i>Meyer-Fong, T. (2013). <i>What Remains: Coming to Terms with Civil War in 19th Century China</i>. Stanford University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/LW63Q9KW"></i>Morgan, C. (2004). The Chinese Game of Shengguan tu. <i>Journal of the American Oriental Society</i>, <i>124</i>(3), 517–532. JSTOR. <a href="https://doi.org/10.2307/4132278">https://doi.org/10.2307/4132278</a></div>
  <div class="csl-entry"><i id="zotero|14298532/C62Y2KVY"></i>Needham, M., &#38; Hodler, A. E. (2019a). <i>Graph Algorithms: Practical Examples in Apache Spark and Neo4j</i>. O’Reilly Media, Inc.</div>
  <div class="csl-entry"><i id="zotero|14298532/LC5FSDKM"></i>Needham, M., &#38; Hodler, A. E. (2019b). <i>Graph Algorithms: Practical Examples in Apache Spark and Neo4j</i>. O’Reilly Media, Inc.</div>
  <div class="csl-entry"><i id="zotero|14298532/5ZHJZ28C"></i>Ngai, M.-Y. M. (2010). <i>From entertainment to enlightenment : a study on a cross-cultural religious board game with emphasis on the Table of Buddha Selection designed by Ouyi Zhixu of the late Ming Dynasty</i> [Ph.D. dissertation, University of British Columbia]. <a href="https://doi.org/10.14288/1.0071581">https://doi.org/10.14288/1.0071581</a></div>
  <div class="csl-entry"><i id="zotero|14298532/W9F7GZR6"></i>Paget R. (2017). Games of Conquest: Sugoroku of Imperial and Wartime Japan. <i>Art in Print</i>, <i>6</i>(5), 24–29. <a href="https://www.jstor.org/stable/26408724?casa_token=a3vD3WpSnAUAAAAA:zVhbT_ImM-7hOVs8QfAUkpmM6eovjh2l_HwpAdrxR0onO5HX9DKEbBDbbhBxPalWgxkAmXMev2kDBjHlZo4DJUTp7OZkkZrVnwk_mGJQoc74Q3xT_nw">https://www.jstor.org/stable/26408724?casa_token=a3vD3WpSnAUAAAAA:zVhbT_ImM-7hOVs8QfAUkpmM6eovjh2l_HwpAdrxR0onO5HX9DKEbBDbbhBxPalWgxkAmXMev2kDBjHlZo4DJUTp7OZkkZrVnwk_mGJQoc74Q3xT_nw</a></div>
  <div class="csl-entry"><i id="zotero|14298532/ZH6Y34YM"></i>Pan, G. 潘國森. (2017). <i>Panshi chongding Qingdai Shengguantu 潘氏重訂清代陞官圖</i>. Showwe Books for Sunyata 新一堂&#38;秀威書店.</div>
  <div class="csl-entry"><i id="zotero|14298532/3D8I6ICQ"></i>Peng, P. (2022). <i>Pen and Sword: Meritocracy, Conflicts, and Bureaucratic Appointments in Imperial China</i> [Ph.D. dissertation]. Duke University.</div>
  <div class="csl-entry"><i id="zotero|14298532/C5VWSXW6"></i>Pilon, M. (2015). <i>The Monopolists: Obsession, Fury, and the Scandal Behind the World’s Favorite Board Game</i>. Bloomsbury Publishing USA.</div>
  <div class="csl-entry"><i id="zotero|14298532/JDFA84RJ"></i>Porter, D. C. (2023). <i>Slaves of the Emperor: Service, Privilege, and Status in the Qing Eight Banners</i>. Columbia University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/V8FFRKCS"></i>Puk Wing Kin 卜永堅. (2011). <i>Youxi guanchang: Shengguantu yu Zhongguo guanzhi wenhua 遊戲官場: 升官圖與中國官制文化</i> (2nd.). Zhonghua Shuju 中華書局.</div>
  <div class="csl-entry"><i id="zotero|14298532/R6IGW83X"></i>Schmidt-Madsen, J. (2019). <i>The Game of Knowledge: Playing at Spiritual Liberation in 18th-and 19th-Century Western India</i> [Ph.D. dissertation]. University of Copenhagen.</div>
  <div class="csl-entry"><i id="zotero|14298532/QPXW5GHH"></i>Seligman, A. B., Weller, R. P., Bennet, S., &#38; Puett, M. J. (2008). <i>Ritual and Its Consequences: An essay on the Limits of Sincerity</i>. Oxford University Press, USA.</div>
  <div class="csl-entry"><i id="zotero|14298532/3JHDWAR9"></i>Seville, A. (2019). <i>The Cultural Legacy of the Royal Game of the Goose: 400 Years of Printed Board Games</i>. Amsterdam University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/8B39GJMI"></i>Stover, L. E. (1974). <i>The Cultural Ecology of Chinese Civilization: Peasants and Elites in the Last of the Agrarian States</i>. Pica Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/FT4X2A27"></i>Sung Ping-Jen 宋秉仁. (2005). Shengguantu youxi yange kao 陞官圖遊戲沿革考. <i>Taiwan Shi Da Lishi Xuebao 臺灣師大歷史學報</i>, <i>33</i>, 27–78. <a href="https://www.airitilibrary.com/Publication/alDetailedMesh?docid=03019667-200506-x-33-27-78-a">https://www.airitilibrary.com/Publication/alDetailedMesh?docid=03019667-200506-x-33-27-78-a</a></div>
  <div class="csl-entry"><i id="zotero|14298532/JQ8Q5PUU"></i>Szita, I., Chaslot, G., &#38; Spronck, P. (2010). Monte-Carlo Tree Search in Settlers of Catan. In H. J. van den Herik &#38; P. Spronck (Eds.), <i>Advances in Computer Games</i> (pp. 21–32). Springer. <a href="https://doi.org/10.1007/978-3-642-12993-3_3">https://doi.org/10.1007/978-3-642-12993-3_3</a></div>
  <div class="csl-entry"><i id="zotero|14298532/CDULDIBZ"></i>Tatz, M., &#38; Kent, J. (1977). <i>Rebirth: The Tibetan Game of Liberation</i>. Anchor Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/PX4XEZRW"></i>Wang, K. 王闓運. (1983). <i>Xiangjun zhi 湘軍志 [History of the Hunan Army]</i>. Yue Lu shushe.</div>
  <div class="csl-entry"><i id="zotero|14298532/LBBMUNK7"></i>Wilkinson, E. (2012). <i>Chinese History: A New Manual</i>. Harvard Asia Center.</div>
  <div class="csl-entry"><i id="zotero|14298532/54772HN8"></i>Will, P.-É. (2020). <i>Handbooks and Anthologies for Officials in Imperial China: A Descriptive and Critical Bibliography</i>. Brill.</div>
  <div class="csl-entry"><i id="zotero|14298532/SLU49A89"></i>Wu Yue 伍跃. (2021). <i>Zhongguo de juanna zhidu yu shehui 中国的捐纳制度与社会</i>. Jiangsu renmin chubanshe.</div>
  <div class="csl-entry"><i id="zotero|14298532/G9J8Z9FU"></i>Wu Yue 伍躍. (2022). Jinshenlu yu Qingdai difang guanyuan renshi zhidu yanjiu 縉紳錄與清代地方官員人事制度研究. <i>Xinya Xuebao 新亞學報</i>, <i>39</i>, 1–62.</div>
  <div class="csl-entry"><i id="zotero|14298532/F8METVWQ"></i>Xu, B. (2021). <i>Chairman Mao’s Children: Generation and the Politics of Memory in China</i>. Cambridge University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/IJAXKZ39"></i>Zhang, L. (2023). <i>Power for a Price: The Purchase of Official Appointments in Qing China</i>. Harvard University Press.</div>
  <div class="csl-entry"><i id="zotero|14298532/UCJTBZXX"></i>Zhang Mingwei 章名未. (2023). Tang Song caixuange yu guanzhi zhishi de chuanbo: yi Liu Ban “Hanguanyi Caixuan” weili 唐宋彩選格與官制知識的傳播：以劉攽《漢官儀彩選》為例. <i>Tang Yanjiu 唐研究</i>, <i>24</i>, 251–271.</div>
</div>
<!-- BIBLIOGRAPHY END -->
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}

```
