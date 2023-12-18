
# Alignment free - TP 2

## Binome
Ce TP a été réalisé par:

Maëlys DELOUIS

Soraya REY 

## Objectifs

Le but de ce TP est, comme le précédent, de réaliser une comparaison entre des génomes en optimisant le temps de calcul et la place en mémoire. Nous utilisons toujours dans ce but une conversion en kmers binaires de chaque séquence, mais effectuons un sampling des kmers les plus petits avant de calculer la distance de Jaccard entre chaque paire de séquence pour estimer l'information partagée. 
Ce sampling est effectué à l'aide d'un objet heapq afin d'optimiser le temps de calcul. Nous avons deux versions: un sampling simple qui se contente de renvoyer les kmers tels qu'ils sont en sortie du stream_kmer (main.py), et une version où les kmers passent au préalable par une fonction xorshift (main_xor.py), afin d'éviter certains biais liés à la nature biologique de nos séquences (par exemple les queues polyA qui sortent systématiquement dans la listes des kmers les plus petits)

## Résultats

Soit s un entier représentant le nombre de kmer selectionné lors du sampling. Nous avons voulu tester différentes tailles de sampling afin de pouvoir comparer nos résultats avec ceux obtenu précédemment en employant tous les kmers.

Pour rappel, nous avions obtenu la matrice de distance suivante :
|Species\Species                              |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.9372829879944679                     |0.0015750639855717137                   |0.01369102282347328                     |0.006857629565735636                    |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.9372829879944679                  |1.0                                    |0.0015815128553124099                   |0.013827493927222058                    |0.006972779039923261                    |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0015750639855717137               |0.0015815128553124099                  |1.0                                     |0.0015892331111325275                   |0.0026831658495443528                   |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.01369102282347328                 |0.013827493927222058                   |0.0015892331111325275                   |1.0                                     |0.18136430081323546                     |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.006857629565735636                |0.006972779039923261                   |0.0026831658495443528                   |0.18136430081323546                     |1.0                                     |

Le temps de calcul était le suivant: 3:34.99 (m:ss)

Et la place occupée en mémoire: 459740 kb

#### s=10
> Sans shift

Temps de calcul: 1:46.46 (mm:ss)

Place en mémoire: 80260 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.42857142857142855                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.42857142857142855                 |1.0                                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.0                                     |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |1.0                                     |0.05263157894736842                     |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |0.05263157894736842                     |1.0                                     |

> Avec shift

Temps de calcul: 2:31.27 (mm:ss)

Place en mémoire: 80260 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.42857142857142855                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.42857142857142855                 |1.0                                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.0                                     |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |1.0                                     |0.1111111111111111                      |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |0.1111111111111111                      |1.0                                     |


#### s=100
> Sans shift

Temps de calcul: 1:45.46 (mm:ss)

Place en mémoire: 80256 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.7857142857142857                     |0.0                                     |0.0                                     |0.0                                     |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.7857142857142857                  |1.0                                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.005025125628140704                    |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |1.0                                     |0.08108108108108109                     |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.0                                 |0.0                                    |0.005025125628140704                    |0.08108108108108109                     |1.0                                     |

> Avec shift

Temps de calcul: 2:32.73 (mm:ss)

Place en mémoire: 80268 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.8018018018018018                     |0.0                                     |0.0                                     |0.0                                     |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.8018018018018018                  |1.0                                    |0.0                                     |0.0                                     |0.0                                     |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.005025125628140704                    |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.0                                 |0.0                                    |0.0                                     |1.0                                     |0.08108108108108109                     |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.0                                 |0.0                                    |0.005025125628140704                    |0.08108108108108109                     |1.0                                     |

#### s=1000
> Sans shift

Temps de calcul: 1:45.64 (mm:ss)

Place en mémoire: 80252 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.9083969465648855                     |0.0                                     |0.009081735620585268                    |0.007556675062972292                    |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.9083969465648855                  |1.0                                    |0.0                                     |0.009081735620585268                    |0.008064516129032258                    |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.002004008016032064                    |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.009081735620585268                |0.009081735620585268                   |0.0                                     |1.0                                     |0.14678899082568808                     |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.007556675062972292                |0.008064516129032258                   |0.002004008016032064                    |0.14678899082568808                     |1.0                                     |

> Avec shift

Temps de calcul:  2:37.03 (mm:ss)

Place en mémoire: 80260 kb

|Species\Species                                  |GCF_000006945.2_ASM694v2_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|
|----------------------------------------|------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|GCF_000006945.2_ASM694v2_genomic.fna    |1.0                                 |0.9083969465648855                     |0.0                                     |0.009591115598182737                    |0.007556675062972292                    |
|GCF_008244785.1_ASM824478v1_genomic.fna |0.9083969465648855                  |1.0                                    |0.0                                     |0.010101010101010102                    |0.008064516129032258                    |
|GCF_014892695.1_ASM1489269v1_genomic.fna|0.0                                 |0.0                                    |1.0                                     |0.0                                     |0.002004008016032064                    |
|GCF_020526745.1_ASM2052674v1_genomic.fna|0.009591115598182737                |0.010101010101010102                   |0.0                                     |1.0                                     |0.1474469305794607                      |
|GCF_020535205.1_ASM2053520v1_genomic.fna|0.007556675062972292                |0.008064516129032258                   |0.002004008016032064                    |0.1474469305794607                      |1.0                                     |


## Analyse
Les deux méthodes ont des résultats numériques assez proches, et, bien que relativement éloignés des valeurs de distance obtenues sur l'ensemble des kmers (par exemple 0.42 entre les deux premières séquences quand s=10, alors que 0.93 était attendu), relativement cohérents. En effet, même avec un très petit échantillon comme s=10, nous sommes capable d'identifier les deux séquences très proches ainsi que la relation plus distante entre les deux dernières séquences de l'ensemble. Elargir la taille du sampling nous fait seulement gagner en précision; à s=1000 on obtient des résultats très proches de ceux attendus. Mais le fait que de petits ensembles nous permettent déjà de mettre à jour une relation entre les séquences nous indique que la décision de prendre les plus petits kmers de l'ensemble est judicieuse car nous avons alors déjà un échantillon représentatif de tous les kmers. 
En termes d'espace en mémoire, le sampling est beaucoup plus efficace puisqu'il divise dans les deux cas l'espace requis par au moins 5. Il n'y a aucune différence à ce niveau entre le sampling simple et le sampling xorshift, ce qui est assez trivial étant donné que la taille d'un entier lors d'un xorshift reste constante. 
Pour ce qui est du temps de calcul, on est dans les deux cas bien en dessous des 3:30 minutes de la version originale. C'était attendu, puisque le sampling permet de réduire le nombre de comparaison paire à paire entre les deux séquences de façon impactante. On remarque également que le xorshift fait perdre du temps de calcul, car l'utilisation de cette méthode a pour conséquence d'ajouter au processus une conversion par kmer, alongeant nécessairement la durée du processus. 
En conclusion, utiliser un sampling peut être très bénéfique en temps et en mémoire puisque les résultats obtenus sont corrects. Il ne faut néanmoins pas s'attendre à beaucoup de précision. Peut-être qu'une autre méthode de sampling permettrait d'obtenir des échantillons plus représentatifs, comme un bootstrap par exemple, mais serait sans doute plus couteux. 
