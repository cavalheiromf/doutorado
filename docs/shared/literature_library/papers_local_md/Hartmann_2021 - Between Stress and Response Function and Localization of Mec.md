# Hartmann_2021 - Between Stress and Response Function and Localization of Mec

**Source PDF:** 

---

               International Journal of
               Molecular Sciences


Review
Between Stress and Response: Function and Localization of
Mechanosensitive Ca2+ Channels in Herbaceous and
Perennial Plants
Félix P. Hartmann * , Erwan Tinturier                      , Jean-Louis Julien and Nathalie Leblanc-Fournier *

                                            Université Clermont Auvergne, INRAE, PIAF, 63000 Clermont-Ferrand, France; erwan.tinturier@uca.fr (E.T.);
                                            J-Louis.Julien@uca.fr (J.-L.J.)
                                            * Correspondence: felix.hartmann@inrae.fr (F.P.H.); nathalie.leblanc@uca.fr (N.L.-F.)


                                            Abstract: Over the past three decades, how plants sense and respond to mechanical stress has become
                                            a flourishing field of research. The pivotal role of mechanosensing in organogenesis and acclimation
                                            was demonstrated in various plants, and links are emerging between gene regulatory networks and
                                            physical forces exerted on tissues. However, how plant cells convert physical signals into chemical
                                            signals remains unclear. Numerous studies have focused on the role played by mechanosensitive
                                            (MS) calcium ion channels MCA, Piezo and OSCA. To complement these data, we combined data
                                            mining and visualization approaches to compare the tissue-specific expression of these genes, taking
                                            advantage of recent single-cell RNA-sequencing data obtained in the root apex and the stem of
         
                                     Arabidopsis and the Populus stem. These analyses raise questions about the relationships between
                                            the localization of MS channels and the localization of stress and responses. Such tissue-specific
Citation: Hartmann, F.P.;
                                            expression studies could help to elucidate the functions of MS channels. Finally, we stress the need
Tinturier, E.; Julien, J.-L.;
Leblanc-Fournier N. Between Stress
                                            for a better understanding of such mechanisms in trees, which are facing mechanical challenges of
and Response: Function and                  much higher magnitudes and over much longer time scales than herbaceous plants, and we mention
Localization of Mechanosensitive            practical applications of plant responsiveness to mechanical stress in agriculture and forestry.
Ca2+ Channels in Herbaceous and
Perennial Plants. Int. J. Mol. Sci. 2021,   Keywords: biomechanics; mechanobiology; mechanosensing; thigmomorphogenesis; calcium chan-
22, 11043. https://doi.org/10.3390/         nels; mechanosensitive channels; MCA; Piezo; OSCA
ijms222011043


Academic Editor: Dorota
Kwiatkowska                                 1. Mechanical Stresses and Responses in Plants
                                            1.1. Ubiquity of Mechanical Stress in Plants
Received: 15 September 2021
Accepted: 7 October 2021
                                                 During their development, plants are exposed to changing and fluctuating mechanical
Published: 13 October 2021
                                            forces, both external and internal [1]. Above ground, transient mechanical loads are caused
                                            chiefly by wind [2], but also by rainfall, snow, animals and neighboring plants. Gravity
Publisher’s Note: MDPI stays neutral
                                            acts permanently, but its magnitude increases with the plant mass and the seasonal bearing
with regard to jurisdictional claims in
                                            of fruits [3], and the lever arm of the weight fluctuates when the plant is swaying in the
published maps and institutional affil-     wind [4]. Under ground, the soil opposes a mechanical resistance to root penetration [5].
iations.                                    In addition, forces exerted above ground are transmitted to the soil, which in turn exerts
                                            reaction forces on the roots. Sessile algae and other aquatic plants are supported by
                                            buoyancy, which counteracts their weight, but they are dragged by currents [6] or tidal
                                            flows [7], and agitated by eddies.
                                                 Even in the absence of external forces, plants are mechanically stressed structures [8].
Copyright: © 2021 by the authors.
Licensee MDPI, Basel, Switzerland.
                                            The primary source of intrinsic stress in plants is turgor pressure in cells, which is coun-
This article is an open access article
                                            terbalanced by stress in the cell wall [9,10]. Within a tissue, a strong stress heterogeneity
distributed under the terms and             is possible between neighboring cells [11], due to differences in cell size or shape [12–14],
conditions of the Creative Commons          but also cell neighbor number [15].
Attribution (CC BY) license (https://            Because cells are rigidly interconnected through their middle lamella, stress is trans-
creativecommons.org/licenses/by/            mitted from one cell to the other and builds up at the tissue scale [16]. This self-induced
4.0/).                                      stress in the tissues is called “tissue stress” [17], “residual stress” [18], or “autostress” [19]



Int. J. Mol. Sci. 2021, 22, 11043. https://doi.org/10.3390/ijms222011043                                         https://www.mdpi.com/journal/ijms
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                   2 of 27




                                    (biologist-friendly definitions of mechanical terms can be found in [20]). Adjacent tissue
                                    layers can be subjected to mutual tension due to tissue shape and/or anatomical differences.
                                    In the shoot apical meristem (SAM) of tomato, the outer cell wall of the epidermal layer
                                    is about seven times thicker than the other cell walls [21]. Being stiffer, the epidermal
                                    layer bears much of the load generated by the turgor of the inner tissue and concen-
                                    trates the stress. This is why the SAM has been described mechanically as a shell under
                                    pressure [22,23]. Similarly, the sunflower hypocotyl, where the outer tissue is stiffer and
                                    under tension while the inner tissue is compressed, has been described as a cylindrical
                                    pressure vessel [24,25]. In these examples, the stress pattern can be predicted based on
                                    tissue shape (Figure 1A). In the epidermis of the elongating Arabidopsis hypocotyl, however,
                                    Verger et al. [16] found that the longitudinal stress is higher than the transverse stress,
                                    which contradicts the cylindrical pressure vessel model. In this example, the stress pattern
                                    is not just based on tissue shape, but predominantly on the anisotropic growth of the inner
                                    tissues, which pulls the epidermis in the longitudinal direction (Figure 1B).


                                    A                                             B             growth




                                    Figure 1. Shape-derived versus growth-derived stress pattern. (A) In the pressure vessel model,
                                    the stress pattern in the epidermis is determined by the shape of the organ. For a cylindrical organ,
                                    the transverse stress is higher than the longitudinal stress. (B) Differential growth between the inner
                                    tissue and the epidermis can override the stress pattern predicted by the pressure vessel model,
                                    leading to a longitudinal stress higher than the transverse stress.

                                         In woody species, additional tissue stress is generated during the maturation of the
                                    secondary cell wall [26,27]. These maturation stresses, when they are asymmetric, act
                                    as adaptive “plant muscles” in the trunk and branches to control posture and cope with
                                    mechanical disturbances [28]. In several tree species, a similar mechanical role is played by
                                    the bark, although based on a different mechanism [29].

                                    1.2. Morphogenesis and Responses to Internal Mechanical Stress
                                         Turgor pressure is the motor of cell growth, but cell growth induces water influx,
                                    which in turn dilutes osmotica in the cell and thus reduces turgor. Therefore, sustaining
                                    the osmohydraulic motor requires a constant adjustment of osmoticum concentration. This
                                    adjustment is thought to involve some sensing of the mechanical state of the cell wall (its
                                    thickness, strain, or stress) and a feedback mechanism on osmoticum influx and efflux [30].
                                         Apart from sustaining cell turgor, responses to mechanical stress are ubiquitous in
                                    plant morphogenesis. A mechanical instability can be the trigger of a reaction cascade lead-
Int. J. Mol. Sci. 2021, 22, 11043                                                                                             3 of 27




                                    ing to a final shape, for instance, the formation of lobes in epidermal pavement cells [31].
                                    Cell pressurization generates hotspots of compressive stress in the anticlinal walls, which
                                    can cause sudden and localized bendings of the wall, a phenomenon termed “buckling”.
                                    The small displacement caused by the buckling is then amplified by a positive-feedback
                                    mechanism involving the cortical microtubules, until a lobe is formed [31]. The global
                                    effect of lobe formation in pavement cells is to keep mechanical stresses low [13]. Could
                                    buckling also initiate leaf primordia in the SAM? Many experimental and numerical results
                                    suggest instead that outgrowths at the meristem surface follow local maxima of the plant
                                    hormone auxin [32–35]. Auxin loosens the cell wall and facilitates organ emergence [36].
                                    However, the polarity of the auxin transporters PIN is influenced by mechanical perturba-
                                    tions, creating a feedback loop between auxin distribution and mechanical stress [37,38].
                                    The outgrowth of a primordium compresses the surrounding tissues. This does not usually
                                    cause buckling, but induces the expression of the homeobox gene SHOOT MERISTEM-
                                    LESS (STM), which marks the boundary domain around primordia and ensures organ
                                    separation [39]. STM expression is quantitatively correlated to curvature in the boundary
                                    domain, which is itself a proxy for mechanical stress. The mechanotransduction pathway
                                    leading to STM expression has been proven to be auxin-independent [39].
                                         The molecular actors through which mechanical stress activates STM are not known.
                                    In many instances, mechanics-driven morphogenesis involves a reorientation of micro-
                                    tubules in response to mechanical stress [22,40,41]. In the periphery of the SAM, micro-
                                    tubules are perpendicular to the direction of maximal strain, whereas they are parallel to the
                                    direction of maximal strain in the boundary between the primordium and the meristem [42].
                                    This shows that while the response of microtubules to mechanical stress or strain is not
                                    completely clear, they are central actors in mechanosensing, including shape sensing [43].
                                    Based on in vitro experiments [44] and in silico simulations [45], Hamant et al. [46] hypoth-
                                    esized that microtubules are sensors of tensile stress direction, or at least sensors of changes
                                    in the tensile stress direction. Microtubules guide the deposition of cellulose microfibrils
                                    on the cell wall [47], thereby locally increasing its resistance to tension and changing the
                                    pattern of stress distribution in a tissue globally. This is how a mechanical feedback loop
                                    could arise and help organs to reach their final shape in a robust way, as neatly exemplified
                                    in the sepal by Hervieux et al. [48,49].

                                    1.3. Thigmomorphogenesis and Responses to External Stress
                                          While internal mechanical stresses play a key role in driving organogenesis until a
                                    determinate target shape is reached, external stresses are inherently unpredictable and
                                    a source of dangerous perturbations. Plants face these challenges through an adaptive
                                    development relying on appropriate responses. This is especially true for perennial plants,
                                    which experience vast changes in size and mass through their life stages, and hence large
                                    variations in external mechanical stress. Adaptation occurs mainly in terms of growth, that
                                    is the addition of material, quantitatively and qualitatively. In trees subjected to transient
                                    bendings, the root biomass increases and the root architecture changes in a way that
                                    improves anchorage [50,51]. The same treatment, mimicking the effect of wind, induces
                                    a reduced height growth and an increased diameter growth in Ulmus americana [52] and
                                    Prunus avium [53], with an ovalization of the stem cross-section along the bending direction.
                                    In poplar, the inhibition of height growth is less significant, but an ovalization has also been
                                    observed [54]. This geometrical change improves the mechanical safety margin of treated
                                    trees [54]. Qualitatively, imposed bendings modulate wood differentiation. In Abies fraseri,
                                    the tracheids formed under bidirectional bending treatment have smaller lumens than in
                                    normal wood and higher microfibril angle [55]. Although bending-induced wood shares
                                    some similarities with compression wood, it has a distinctive anatomical structure and has
                                    been termed “flexure wood” by Telewski [55]. In poplar, transient unidirectional bendings
                                    cause a decrease in vessel frequency and an increase in the thickness of the secondary
                                    cell wall of fibers [56]. Unlike bidirectional bendings, unidirectional bendings allow the
                                    observation of differential effects between the stretched and compressed sides of the bent
Int. J. Mol. Sci. 2021, 22, 11043                                                                                             4 of 27




                                    stem. For instance, vessel size is decreased in the stretched side only [56]. Thus, while
                                    radial growth depends on the absolute magnitude of strains, wood-forming tissues have
                                    the ability to distinguish between positive and negative strains. Overall, wood produced
                                    under mechanical stress is more resistant to damage and enhances the bending strength of
                                    the stem [57].
                                         These various manifestations of growth acclimation to mechanical perturbations are
                                    collectively termed “thigmomorphogenesis” [58]. Thigmomorphogenesis tends toward
                                    better self-support and increased resistance of trees to wind [59]. Despite its high cost in
                                    terms of biomass allocation, it is a priority requirement for trees, even under severe water
                                    stress [54]. Tree acclimation to wind loads has been demonstrated not only in controlled
                                    experiments but also in a forest context [60]. Although most striking in perennials, thigmo-
                                    morphogenesis has also been reported in herbaceous plants, for instance Arabidopsis [61,62]
                                    and Plantago major [63], and aquatic plants [64].

                                    1.4. Localized versus Distant Responses
                                          Mechanical actions can be very localized and initiate equally localized responses.
                                    For example, the emergence of a lateral root can be a response to a local bending [65,66].
                                    Lateral root emergence is also an example of mechanical stress exerted from inside. The lat-
                                    eral root can emerge only if the epidermis yields to internal pressure. This is mediated by a
                                    complex signaling cascade, which modulates the mechanical properties of cell walls [67].
                                    External stresses are exerted by the soil on the progressing root cap. When a poplar root
                                    encounters a physical obstacle, its growth rate sharply decreases, even before the force
                                    builds up at the contact point [68]. This early growth response is most likely induced by
                                    the mechanosensing of very small forces on the root cap. In laboratory conditions, when
                                    the root is growing in a nutrient solution and is free to move laterally, the force exerted
                                    on the obstacle increases progressively until the root buckles [68]. If the root is laterally
                                    supported, such as in a natural environment, it can reach an axial force much larger than
                                    the buckling threshold [68].
                                          To investigate the ability of Arabidopsis roots to progress in a medium with varying
                                    strength, Roué et al. [69] designed an experimental setup consisting of two layers of growth
                                    medium containing Phytagel at different concentrations. The lower layer has a higher
                                    concentration and is consequently more resistant to penetration, mimicking a more compact
                                    soil layer. Upon contact with the interface between the two layers, the root either penetrates
                                    the lower layer or reorients its growth [69]. Arabidopsis genotypes exhibiting contrasted root
                                    cap morphologies have different penetration abilities. The fez-2 loss-of-function mutant,
                                    with a pointed cap, penetrates less often the denser layer than the Col-0 wild type, which
                                    in turn has a lower penetration ability than the smb-3 loss-of-function mutant, with a
                                    rectangular-shaped cap [69]. It is yet to be determined whether these unequal penetration
                                    abilities are caused solely by differences in root cap morphology, or results from possible
                                    mutation-induced alterations of the mechanical rigidity or mechanosensitivity of the root
                                    cap. Non-penetrating roots of all three genotypes undergo a rapid curving interpreted as
                                    passive buckling. In some cases, especially when the change in medium strength across
                                    the interface is highest, the buckling deviates the root apex in the horizontal direction and,
                                    later, a second curving reorients the apex to the vertical. This second curving is interpreted
                                    as an active movement resulting from the interaction between gravitropic and thigmotropic
                                    responses [69].
                                          Responses can also occur far away from the stimuli. In manually bent tomato plants,
                                    although only the basal part of the stem directly experiences a mechanical stress, a growth
                                    response is also observed in distant primary meristems in the form of reduced height
                                    growth [70]. Since the estimated velocity of this long-distance signaling is incompatible
                                    with hormone transport [71], it is either hydraulic [72,73] or electrical [74] in nature. In Ara-
                                    bidopsis, long-distance signaling is also observed after mechanical wounding [75]. Tissues
                                    far from the wound rapidly synthesize jasmonates, which have been proven to enhance
                                    pest resistance and regulate growth [76]. Farmer et al. [77] hypothesized that the hydraulic
Int. J. Mol. Sci. 2021, 22, 11043                                                                                         5 of 27




                                    and electrical signals induced by a wound could be mechanically coupled. After wounding,
                                    a traveling pressure wave increases locally and abruptly turgor in xylem vessels, which
                                    in turn exert strong pressure on adjacent cells. According to the so-called “squeeze cell
                                    hypothesis”, mechanical stress in squeezed adjacent cells activates Ca2+ channels, causing
                                    ion fluxes, which propagate from cell to cell.
                                          In poplars, local flame wounding on the stem alters stem elongation and stimulates,
                                    in stem apices, the expression of JAZ5, a gene encoding Jasmonate-ZIM domain protein [78].
                                    On the other hand, moderate poplar stem bending does not trigger any remote response [78]
                                    although it induces a long-distance electrical signal [74]. A possible explanation could be
                                    that a moderate bending does not cause a wound, and therefore induces a weaker signal,
                                    which attenuates over a shorter distance [74]. This would also explain why tomato plants,
                                    which are short, display a remote growth response to bending [70], whereas in bent poplar
                                    the electrical signal cannot travel the longer distance between the wounding point and the
                                    stem apex.
                                          As a conclusion, plants respond to mechanical stress in many different ways. However,
                                    responding to a stress is only possible if the stress is perceived. Mechanosensing and
                                    mechanotransduction have hence been the focus of numerous studies using the powerful
                                    tools of molecular biology. The next two sections of this review will be devoted to the
                                    description of some molecular actors of mechanosensing and how they can be related to
                                    the growth and development of roots and stems.

                                    2. Mechanosensitive Channels across the Plant Kingdom
                                    2.1. Diversity of Mechanosensing Mechanisms
                                          As described in the previous section, cells from diverse tissues detect mechanical
                                    signals through potentially diverse mechanisms, triggering different biological responses.
                                    These different types of mechanical stresses (e.g., bending, dryness or hyperosmotic shock)
                                    cause stretching of the plasma membrane, displacement of the plasma membrane relative to
                                    the cell wall (e.g., cell-wall loosening during cell expansion, hypo-osmotic shock), changes
                                    in the orientation of cortical microtubules [22] and could also affect the nucleus through
                                    interactions between cellular compartments via the cytoskeleton [79]. The perception of a
                                    mechanical stress by a cell is a rapid process requiring a quick conversion of a mechanical
                                    signal into a biological signal. Major progress has been made in recent years in identifying
                                    the molecular players involved in mechanosensing. Two major types of candidates emerge
                                    from these studies: (i) receptor-like kinases from Catharanthus roseus RLK1-like subfamily
                                    (CrRLK1) identified in approaches aimed at studying the maintenance of cell wall integrity
                                    (see review by Bacete and Hamman [80] and references therein), and (ii) mechanosensitive
                                    (MS) ion channels (see review by Frachisse et al. [81] and references therein).
                                          Among the CrRLK1 family, FERONIA is a player at the interface of many responses
                                    involving the perception of mechanical stresses. Thus, besides its well-known role in
                                    cell growth and hormone signaling [82], the fer loss-of-function mutant has impaired ion
                                    signaling, reduced expression of mechanoresponsive genes and altered root growth re-
                                    sponses to mechanically challenging environments when exposed to local touch or bending
                                    stimulation [83]. Furthermore, FERONIA also appears to play a role in developmental
                                    responses involving the perception of mechanical stimuli such as root nutation [84], root
                                    gravitropism [85], roots encountering an impenetrable cover glass barrier [83]. This trans-
                                    membrane protein has an extracellular domain containing two MALECTIN-like domains
                                    that may be involved in binding to cell wall components and an intracellular kinase domain
                                    that may trigger phosphorylation-dependent signaling pathways during mechanotransduc-
                                    tion. Interestingly, a recent work shows the involvement of several phosphoproteins—MAP
                                    kinase kinase (MKK) and a novel protein named TREPH1—in the process of the most-
                                    studied thigmomorphogenetic response in Arabidopsis, i.e., the emergence of the flowering
                                    stem [86].
                                          The other important actors are the MS channels, which are inserted in the membrane
                                    and function as ion transporters across the membrane when under mechanical stress. They
Int. J. Mol. Sci. 2021, 22, 11043                                                                                             6 of 27




                                    are prime candidates for converting a mechanical signal into a chemical signal. Described
                                    in various reviews [81,87,88], several types of MS channels have been identified in plants,
                                    including the anion-permeable channel MSL and several types of calcium-permeable
                                    channels families such as MCA, Piezo and OSCA.
                                          Another way to understand the early stages of mechanosensing is to follow the dynam-
                                    ics of intracellular calcium concentrations. Indeed, calcium cations are typically involved as
                                    quick secondary messengers in numerous plant responses [89]. A rapid increase in concen-
                                    tration of cytosolic Ca2+ ions occurs in response to mechanical stimuli such as touch, wind
                                    or osmotic variations in plants [90–93], triggering a specific local response, but also possibly
                                    causing distant responses by propagating electrical signals [94,95]. The diversity of calcium
                                    signatures depending on the nature of the mechanical stimuli is very well described in
                                    the study carried out by Monshausen et al. [67] on the Arabidopsis root. In this study,
                                    the authors showed that touch, bending or root growth against an impenetrable barrier
                                    trigger a rapid (<30 s) increase in intracellular calcium. However, the calcium signatures
                                    are different in duration and in the peak intensity, suggesting the potential involvement
                                    of different mechanosensing mechanisms or the importance of a sensitivity threshold. It
                                    is also important to note that, in the case of bending stimulus, the calcium increase is
                                    visible mainly in the tensile tissues of the root, suggesting potentially different sensing
                                    mechanisms between compressive and tensile strains. Moreover, the calcium response is
                                    biphasic, involving two peaks of different intensities. The channels involved in this calcium
                                    response have not been identified to date. However, FERONIA seems to be involved in
                                    this response since fer loss-of-function mutants subjected to such mechanical stimulation
                                    do not show the second calcium peak, characteristic of this biphasic response. However,
                                    the calcium-permeable channels responsible for the first calcium peak and the role of
                                    FERONIA in triggering the second calcium peak remain to be identified. Shih et al. [83]
                                    report that under their conditions, the loss-of-function mutant mca1 and the quintuple
                                    mutant msl4 msl5 msl6 msl9 msl10 are not impaired in this response.
                                          Given the predominant position of the calcium-permeable channels in the literature on
                                    plant mechanotransduction, we will focus in the rest of this section on this mechanosensing
                                    mechanism. It should also be noted that the genes involved in the calcium signaling
                                    pathway such as calmodulins were among the first genes discovered to be regulated at the
                                    transcriptional level by mechanical stimuli [96].

                                    2.2. Description and Functioning of Mechanosensitive Ca2+ Channels
                                    2.2.1. The Mid1-Complementing Activity (MCA) Family
                                         The MCA family was first described in Arabidopsis thaliana [97]. AtMCA1 and AtMCA2
                                    are paralogs, with high sequence homology (the relationships between gene names and
                                    accession numbers are given in Table S1).
                                         The MCA channel was thought to be organized as a homotetramer with a small trans-
                                    membrane region forming the pore (with only one transmembrane domain per monomer)
                                    and a larger cytoplasmic region of motifs (an EF hand-like motif, a coiled-coil motif and
                                    a cysteine-rich region homologous to the PLAC8 or DUF614 motif near the carboxyl ter-
                                    minus) regulating the pore [98–100]. While the PLAC8 domain is observed in eukaryotic
                                    proteins, its combination with the transmembrane domain and the EF hand-like motif is
                                    specific to streptophytes, and absent in chlorophytes (Figure 2A). Therefore, in contrast
                                    to other MS channels (Figure 2), MCA appears to be specific to land plants [101]. This
                                    may relate to the specific selective pressure faced by land plants, which can not rely on
                                    water buoyancy to support themselves and hence developed posture control mechanisms
                                    to maintain an erect habit [4]. However, it is not known whether MCA genes are directly
                                    involved in posture control.
                                         Even if a fine analysis of the electrophysiological properties of this MS channel is
                                    lacking, MCA1-expressing Xenopus laevis oocytes enhances ionic currents following me-
                                    chanical stimuli such as hypo-osmotic shock or in response to negative pressure in the patch
                                    pipette [97,102]. In vivo, AtMCA1 appears to be involved in Ca2+ uptake in Arabidopsis
Int. J. Mol. Sci. 2021, 22, 11043                                                                                           7 of 27




                                    thaliana roots [103]. It is also thought to be crucial in the process of root penetration in a
                                    hard agar medium [97]. Indeed, using a two-phase agar method, Nakagawa et al. [97]
                                    demonstrated that the primary roots of mca1-null plants fail to penetrate a harder agar
                                    medium from a softer one, whereas mca2-null seedlings are able to grow like wild-type
                                    (WT) plants depending on the hardness of agar medium [103].
                                          Hypergravity has the effect of inhibiting the growth of the hypocotyl of Arabidopsis
                                    thaliana. This effect is reduced in an mca-null mutant compared to WT, and is enhanced in
                                    an MCA-overexpressing mutant [104]. These results also suggest the involvement of MCA
                                    in gravity perception.

                                    2.2.2. The Piezo Family
                                          First identified in vertebrates, the mechanically-activated Piezo family (Figure 2B) is
                                    conserved with homologs in prokaryotes, plants, and invertebrates [105].
                                          In vertebrates, Piezo 1 and 2 are large structures of approximately 2500 amino-acids
                                    including many transmembrane regions. Cryo-electron microscopy (cryo-EM) studies have
                                    shown that Piezo1 possesses a tree-bladed, homotrimeric structure comprising a central
                                    ion-conducting pore module [106–109]. Each peripheral blade has 38 transmembrane
                                    regions, with the peripheral blade-like structures on the extracellular side and three beams
                                    on the intracellular side. With its distal blades and the central pore, the Piezo1 channel
                                    could have a lever-like mechanotransduction mechanism that could explain how it converts
                                    mechanical forces into a cation influx (see the illustrated model proposed in [110]).
                                          In vertebrates, Piezo 1 and 2 are mechanotransducers able to convert a mechanical
                                    force into an increase in cytosolic Ca2+ , enhancing various Ca2+ -dependent downstream
                                    signaling pathways. Piezo1 can be activated by a large variety of mechanical stimula-
                                    tion such as poking, stretching or any local membrane tension, while Piezo2 seems to
                                    be strongly activated only by poking. In Arabidopsis, Mousavi et al. [111] studied the
                                    electrophysiological properties of the unique Piezo protein via a chimeric PZO1 construct
                                    including the C-terminal part of AtPiezo1 (containing the putative pore region) and the
                                    N-terminal part of the mouse mPiezo1 to allow the anchoring of the protein in the plasma
                                    membrane. They showed that this chimeric PZO1 protein is functional and acts as an MS
                                    channel when expressed in naive mammalian cells.
                                          Piezo ion channels play key roles in mechanobiological processes in animals, for ex-
                                    ample, in vascular development or touch sensing [112]. In plants, their role is still largely
                                    unknown, with only four studies to date. In Arabidopsis thaliana, AtPiezo is a key element
                                    of the immune response to the cucumber mosaic virus and the turnip mosaic virus [113].
                                    In addition, several recent works have made major advances on the potential role of At-
                                    Piezo in Arabidopsis root growth in responses to substrate impedance [111,114]. When
                                    atpiezo null-mutant plants were grown in vitro in vertical plates leading to root growth on
                                    the surface of the medium, no difference was observed from WT plants [114]. However,
                                    when the plants were grown in a horizontally placed plate with 0.8% agar, the root ability
                                    to penetrate the medium decreased by about 20% compared to WT. Similar results were
                                    obtained by Mousavi et al. [111], who showed that when seedling roots grew within the
                                    Murashige and Skoog medium, the length of the mutant roots were shorter compared to
                                    WT. Both studies suggest a direct role of AtPiezo in mechanosensing in roots. Interestingly,
                                    as detected for Atmca1 [103], in these two studies, reporter gene expression of Piezo::GUS
                                    in transgenic Arabidopsis thaliana plants showed that AtPiezo is mainly expressed in the root
                                    cap in a cross-section of the root tip.
                                          However, in moss (Physcomitrium patens), PpPiezo1 and 2 are localized in the tonoplast
                                    and are thought to be involved in the regulation of vacuole shape in apical caulonemal
                                    cells [115]. These results raise the question of the role of the vacuole in mechanosensing.
                                    A study linking cellular elongation, vacuole expansion and the role of FERONIA has been
                                    carried out by Dünser et al. [116]. Using epidermal atrichoblast root cells and by combining
                                    different fluorescent dyes in cellular compartments, they showed that the cytosol shows
                                    relatively minor volume expansion during epidermal elongation compared to the relative
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                        8 of 27




                                    increase in vacuolar size. By using different approaches, they investigated the possibility
                                    that apoplast acidification/cell wall loosening is sensed and provides a feedback control for
                                    vacuolar morphogenesis. Again, fer loss-of-function mutant vacuoles were markedly less
                                    affected by extracellular constraints of the substrate suggesting a role of a FER-dependent
                                    signaling in regulating the intracellular expansion of the vacuole. It would be interesting
                                    to analyze if Piezo could be involved in these mechanisms.

                                      A          MCA
                                                                          Metazoa   Fungi
                                                                                                         Viridiplantae

                                                               Protozoa




                                              Euryarchaeota




                                                                                                         Pentapetalae (Eudicotyledons)
                                          Archaea




                                                                                            Firmicutes




                                                       Bacteria


                                      B          Piezo
                                                                          Metazoa   Fungi                Viridiplantae

                                                               Protozoa




                                               Euryarchaeota




                                                                                                         Pentapetalae (Eudicotyledons)
                                          Archaea
                                                                                            Firmicutes




                                                       Bacteria


                                      C         OSCA
                                                                          Metazoa   Fungi                Viridiplantae

                                                               Protozoa




                                              Euryarchaeota




                                                                                                         Pentapetalae (Eudicotyledons)
                                          Archaea
                                                                                            Firmicutes




                                                       Bacteria


                                    Figure 2. Presence of the MCA (A), Piezo (B) and OSCA (C) families in the tree of life. See Appendix A
                                    for details.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                            9 of 27




                                    2.2.3. The OSCA Family, Hyperosmolarity-Gated Calcium-Permeable Channels
                                          OSCA is the largest family of mechanically-activated ion channels identified and con-
                                    served across eukaryotes, including fungi, animals (homologous TMEM63 channels) and
                                    plants (Figure 2C) [117,118]. In Arabidopsis thaliana and Populus trichocarpa, OSCA is com-
                                    posed of 15 and 17 genes, respectively, separated in four clades (Figure 3). Murthy et al. [118]
                                    tested the mechanosensitivity of channels across clades by selecting one gene from each
                                    clade in Arabidopsis thaliana. Electrophysiological results suggest that the channels encoded
                                    by the three genes AtOSCA1.8, AtOSCA2.3, and AtOSCA3.1 are mechanosensitive, a trait
                                    that would not be found for the AtOSCA4.1 channel (Murthy et al., 2018). Clade 4 shares
                                    the least homology with clade 1 (Figure 3). AtOSCA4.1 may have a distinct function.
                                          Cryo-EM studies revealed a molecular structure formed by a homodimer with two
                                    pores [119–121]. Work on AtOSCA1.1 and AtOSCA1.2 suggests that the resulting pores are
                                    non-selectively permeable to cations [118]. Each subunit is composed of 11 transmembrane
                                    domains, as well as a soluble cytosolic domain with an RNA recognition motif. The cytoso-
                                    lic domain has a distinct structural feature in the form of extended intracellular helical arms
                                    parallel to the plasma membrane. These arms are well positioned to detect a change in the
                                    lateral tension of the inner lipid bilayer sheet caused by a change in turgor pressure [122].
                                    Membrane topology appears to be conserved across eukaryotes [118].
                                          The physiological functions of OSCA channels remain poorly understood. Until now,
                                    several studies have implicated the OSCA genes in osmotic responses. However, a hypo-
                                    or hyper-osmotic shock results in a stretching or a relaxation of the plasma membrane,
                                    and can be considered as a mechanical stimulation. AtOSCA1.1 mediates osmotic sig-
                                    naling in guard cells and roots cells, and attenuates water transpiration and root growth
                                    in response to osmotic stress [123]. AtOSCA1.3 controls plant stomatal immunity [124].
                                    In maize, ZmOSCA2.4 has been shown to be involved in drought tolerance in transgenic
                                    Arabidopsis [125]. Recently, an RNA-seq study by Procko et al. [126] suggested an involve-
                                    ment of the MS channels MSL and OSCA in triggering the touch-sensitive hair of the Venus
                                    flytrap (Dionaea muscipula). It would be interesting to see whether OSCA channels have a
                                    role in other mechanical processes.
                                          The diversity of calcium-permeable MS channels present in plants could explain what
                                    makes a mechanically-induced [Ca2+ ]cyt signaling pattern specific (Ca2+ footsprint), leading
                                    ultimately to a specific, graded physiological response. As very well explained in a recent
                                    review by Frachisse et al. [81], the detailed characterization of the electrophysiological
                                    properties of these different channels shows that they differ in their permeation and gating
                                    properties (activation threshold, conductance, inactivation). They can therefore trigger
                                    distinct signaling pathways and potentially be activated differentially, depending on the
                                    magnitude of the mechanical stress.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                 10 of 27




                                                                       Clade 1                              PtOSCA1.1
                                                                                                            PtOSCA1.2
                                                                                                            PtOSCA1.3
                                                                                                            PtOSCA1.4
                                                                                                            PtOSCA1.5
                                                                                                            AtOSCA1.1
                                                                                                            AtOSCA1.2
                                                                                                            AtOSCA1.3
                                                                                                            AtOSCA1.4
                                                                                                            PtOSCA1.6
                                                                                                            PtOSCA1.7
                                                                                                            AtOSCA1.5
                                                                                                            AtOSCA1.6
                                                                                                            AtOSCA1.7
                                                                                                            AtOSCA1.8
                                                                                                            PtOSCA1.8
                                                                                                            PtOSCA1.9
                                                                       Clade 3                              PtOSCA3.1
                                                                                                            AtOSCA3.1
                                                                                                            AtOSCA4.1
                                                                       Clade 4
                                                                                                            PtOSCA4.1
                                                                                                            PtOSCA4.2
                                                                       Clade 2                              PtOSCA2.1
                                                                                                            AtOSCA2.5
                                                                                                            PtOSCA2.2
                                                                                                            AtOSCA2.1
                                                                                                            AtOSCA2.2
                                                                                                            PtOSCA2.3
                                                                                                            AtOSCA2.3
                                                                                                            AtOSCA2.4
                                                                                                            PtOSCA2.4
                                                                                                            PtOSCA2.5

                                    Figure 3. Maximum-likelihood phylogenetic tree of OSCA of Arabidopsis thaliana and Populus tri-
                                    chocarpa. The percentage of trees in which the associated taxa clustered together is shown next to the
                                    branches. Initial trees for the heuristic search were obtained automatically by applying Neighbor-Join
                                    and BioNJ algorithms to a matrix of pairwise distances estimated using the JTT model, and then
                                    selecting the topology with a superior log-likelihood value. The tree is drawn to scale, with branch
                                    lengths measured in number of substitutions per site. This analysis involved 22 amino acid sequences.
                                    All positions with less than 50% site coverage were eliminated, i.e., fewer than 50% alignment gaps,
                                    missing data, and ambiguous bases were allowed at any position (partial deletion option). There
                                    were a total of 770 positions in the final dataset. Evolutionary analyses were conducted in MEGA X.
                                    The four clades are colored: blue (Clade 1), yellow (Clade 2), green (Clade 3), and orange (Clade 4).
Int. J. Mol. Sci. 2021, 22, 11043                                                                                             11 of 27




                                    3. Mechanosensitive Channels in Tissues and Organs
                                         The functions of the different families of MS channels are far from being fully un-
                                    derstood. Several questions remain to be answered regarding their role during either
                                    development or acclimation to external mechanical stress. Are there relationships between
                                    the localization of MS channels and the localization of stress and responses? Is the number
                                    of different types of these channels in a membrane responsible for a difference in the
                                    sensitivity of cells to membrane stretch? Within a multigene family, is there redundancy
                                    between proteins or are they specifically localized in tissues? Do these different channels
                                    interact in the same signalization pathways? In relation to these questions, the most-
                                    studied family of MS channels is the anion-preferring MSL family [88]. Within this MSL
                                    family, consisting of 10 members in Arabidopsis, some isoforms localize in membranes
                                    of different cell compartments (plasma membrane, tonoplast, mitochondrial membrane)
                                    and are expressed in a tissue-specific manner. Concerning calcium-permeable channels,
                                    MCA and OSCA channels are located in the plasma membrane [97,123], whereas Piezo1 is
                                    located in the tonoplast [115]. However, information is incomplete regarding the location
                                    of their expression.
                                         Studying the regulation and the localization of the expression of these genes could
                                    help to design new hypotheses on their function. In this section, through data mining
                                    and visualization, we compare the tissue-specific expression of these three families of MS
                                    channels in plants, focusing on root and stem tissues. In Arabidopsis, recent studies using
                                    RNA-seq approaches carried out on single cells have revealed the expression of thousands
                                    of genes in different root tissues [127] or in tissues of the floral stem [128]. We also studied
                                    the expression profiles of members of these families in poplar using RNA-seq data obtained
                                    by Sundell et al. [129] from laser dissection of stems comprising developing phloem and
                                    secondary xylem.

                                    3.1. Mechanosensitive Channel Expression in the Root Tip
                                         As root cap cells are the first to encounter obstacles, this tissue is a potential mechanosens-
                                    ing site. Therefore, the molecular mechanisms underlying root-obstacle avoidance has
                                    been the subject of much research in recent years. To mimic the progression of the root in
                                    the face of mechanical stresses related to soil impedance, studies were conducted using
                                    several in vitro systems: artificial root barrier systems or experimental setups consisting of
                                    two layers of growth medium containing Phytagel at different concentrations to modify
                                    the physical strength of the medium [69]. The typical responses of roots encountering
                                    an obstacle are a reduction of root growth and a resulting “step-like” growth pattern,
                                    with only the root tip remaining in contact with the barrier surface. By RNA-seq ap-
                                    proaches performed on whole roots of Arabidopsis seedlings collected either 6 or 30 h after
                                    barrier contact, combined with reporter line and mutant studies, Jacobsen et al. [130]
                                    showed significant changes in reactive oxygen species (ROS), ethylene and auxin signaling
                                    pathways, confirming several previous studies. In particular, they demonstrated that when
                                    ethylene signaling is perturbed in ethylene-insensitive mutants, the root growth is less
                                    inhibited than in WT after barrier contact. In the same way, auxin transport effects were
                                    observed through altered bending responses, which is consistent with other studies using
                                    PIN-mutants, pharmacological assays and image analysis [131].
                                         Meanwhile, in the last fifteen years, several studies have evidenced the role of MS
                                    channels in root responses to mechanical impedance stress. However, tissue-specific
                                    mecanosensing and the role of the different MS channels are far from being well-understood.
                                    So far, no link between the activation of auxin, ROS and ethylene signaling pathways and
                                    the activation of MS channels have been demonstrated during the root response to substrate
                                    impedance. Furthermore, in vivo root growth dynamics and the root trajectory following
                                    the contact of the root apex have not been finely analyzed in mca-mutants or piezo-mutant of
                                    Arabidopsis thaliana. Using different root-cap development mutants, this type of approach
                                    has shown that the shape of the root cap and the growth rate of the root are parameters that
                                    strongly influence the mechanical resistance of the root to buckling or the magnitude of the
Int. J. Mol. Sci. 2021, 22, 11043                                                                                          12 of 27




                                    force applied by the root on the substrate [69]. If such anatomical or growth defects were
                                    found in these mutants, these parameters could influence the ability of Arabidopsis roots
                                    to progress in a medium with varying strength. In addition, the growth arrest observed
                                    following contact of the root with the substrate suggests a change in cell elongation, at a
                                    distance from the contact point, in the elongation zone. How is the signal transmitted?
                                    Are the innermost cells deformed and respond to this mechanical stress? Could the OSCA
                                    genes play a role in this response?
                                         To study the location of the expression of these different genes in different cell types
                                    of the root, we compared their tissue-specific expression using novel visualizations of data
                                    obtained by Ryu et al. [127] with the single-cell RNA-seq method.
                                         When using a common scale to compare the expression levels of all tested genes
                                    (Figure A1), it appears clearly that AtOSCA2.4 and AtOSCA3.1 reach the highest level
                                    of expression in the tissues composing the root. While AtOSCA2.4 is most highly ex-
                                    pressed in the outermost tissues (epidermis, cortex, lateral cap and columella), AtOSCA3.1
                                    expression is high in the phloem and cortex and at a lower level in the columella and epi-
                                    dermis. The genes AtMCA2, AtOSCA1.4, AtOSCA1.5, AtOSCA1.6, AtOSCA1.7, AtOSCA2.5,
                                    AtOSCA4.1 and AtPiezo show a 10-fold lower expression level than the other genes. How-
                                    ever, when the expression levels of these genes are plotted on a scale specific to each gene
                                    (Figure 4), very distinct expression profiles emerge. For example, AtOSCA2.5 appears
                                    to be expressed in cap tissues, AtOSCA1.5 in the pericycle, AtOSCA1.7 in the phloem,
                                    AtMCA2 in the endodermis and AtOSCA1.4 in epidermal cells developing a root hair. Al-
                                    though low, the tissues with the highest amount of AtPiezo transcripts are the cortex, lateral
                                    cap, and xylem. These data are in agreement with the histochemical approaches using
                                    the GUS reporter gene highlighted by Mousavi et al. [111], although this transcriptomic
                                    approach, which allows a stronger differentiation of expression levels, shows that AtPiezo
                                    expression in the columella is relatively low. Similarly, the tissue-specific expression of
                                    AtMCA1 in the columella and xylem was revealed by Yamanaka et al. [103]. Regarding the
                                    vascular tissues of the stem, apart from AtOSCA2.1, the genes of the OSCA family show
                                    a higher expression in the phloem in contrast to AtMCA1 and AtPiezo. Concerning the
                                    OSCA gene family, it is interesting to observe that genes that are very close in sequence and
                                    probably originate from the same duplication event (see the phylogenetic tree Figure 3) can
                                    present very different expression profiles (e.g., AtOSCA1.1 and AtOSCA1.2, or AtOSCA2.1
                                    and AtOSCA2.2). These results suggest that these proteins may be involved in different
                                    physiological functions. The expression of many OSCA genes in the lateral cap or columella
                                    (AtOSCA1.1, AtOSCA1.3, AtOSCA2.3, AtOSCA2.5) could encourage studies on their role
                                    in root penetration or in the perception of water stress at the root level. In the context of
                                    mechanosensing, it would also be interesting to study AtOSCA2.4 and AtOSCA1.4, which
                                    show, respectively, strong and specific expression in rapidly-expanding epidermal cells.
                                    In contrast, the expression level of all these genes encoding MS channels is very low in the
                                    meristematic zone.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                       13 of 27




                                                                                                        AtMCA1               AtMCA2
                                           pericycle      phloem      xylem                                                             0.030
                                                                                                                   0.30
                                        endodermis                                                                                      0.025
                                             cortex                                                                0.25
                                                                                   root hair                                            0.020
                                          epidermis                                                                0.20
                                                                              meristematic                                              0.015
                                                lateral                          zone                              0.15
                                               root cap                                                                                 0.010
                                                                                                                   0.10
                                                                      columella                                    0.05                 0.005

                                                                                                                                        0.000
                                         AtOSCA1.1                     AtOSCA1.2                       AtOSCA1.3            AtOSCA1.4
                                                              0.175                            0.35                                     0.08
                                                                                                                   0.35
                                                              0.150                            0.30                                     0.07
                                                                                                                   0.30
                                                                                                                                        0.06
                                                              0.125                            0.25                0.25
                                                                                                                                        0.05
                                                              0.100                            0.20                0.20
                                                                                                                                        0.04
                                                              0.075                            0.15                0.15                 0.03
                                                              0.050                                                0.10                 0.02
                                                                                               0.10
                                                              0.025                                                0.05                 0.01
                                                                                               0.05
                                                              0.000                                                                     0.00
                                         AtOSCA1.5                     AtOSCA1.6                       AtOSCA1.7            AtOSCA1.8
                                                              0.040                            0.007
                                                                                                                   0.008                0.30
                                                              0.035                            0.006
                                                                                                                   0.007                0.25
                                                              0.030
                                                                                               0.005               0.006
                                                              0.025                                                                     0.20
                                                                                               0.004               0.005
                                                              0.020                                                0.004
                                                                                               0.003                                    0.15
                                                              0.015                                                0.003
                                                                                               0.002                                    0.10
                                                              0.010                                                0.002
                                                              0.005                            0.001               0.001                0.05
                                                                                               0.000               0.000
                                         AtOSCA2.1                     AtOSCA2.2                       AtOSCA2.3            AtOSCA2.4
                                                              0.14                                                 0.10
                                                                                                                                        0.8
                                                                                               0.25                0.09
                                                              0.12                                                                      0.7
                                                                                                                   0.08
                                                                                                                                        0.6
                                                              0.10                             0.20                0.07                 0.5
                                                              0.08                                                 0.06                 0.4
                                                                                               0.15
                                                                                                                   0.05                 0.3
                                                              0.06                                                 0.04
                                                                                               0.10                                     0.2
                                                              0.04                                                 0.03                 0.1
                                                                                               0.05

                                         AtOSCA2.5                     AtOSCA3.1                       AtOSCA4.1            AtPiezo1
                                                                                                                   0.0275
                                                              0.05                             0.8                 0.0250               0.06

                                                              0.04                             0.7                 0.0225
                                                                                                                                        0.05
                                                                                               0.6                 0.0200
                                                              0.03                                                                      0.04
                                                                                                                   0.0175
                                                                                               0.5
                                                              0.02                                                 0.0150
                                                                                               0.4                                      0.03
                                                                                                                   0.0125
                                                              0.01                             0.3                 0.0100               0.02
                                                              0.00                             0.2

                                    Figure 4. Expression patterns of MCA, Piezo and OSCA genes in different tissues of the Arabidopsis
                                    root. Data for each gene were retrieved from the BAR ePlantArabidospsis website (https://bar.
                                    utoronto.ca/eplant, accessed on 23 February 2021). To facilitate the graphical representation of
                                    expression levels in tissues, only expression values from sub-clusters containing differentiated (not
                                    differentiating) cells were used. In the stele, only the expression data from xylem- and phloem-cell
                                    types are shown. In the meristematic zone, we represented the expression mean of dividing cells
                                    and cells from the quiescent center. See Appendix B.1 for details and Table S1 for the relationships
                                    between gene names and accession numbers.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                            14 of 27




                                    3.2. Mechanosensitive Channels Expression in the Stem
                                          Like in the root, cells in the plant stem are sensitive to external mechanical stress
                                    during primary or secondary growth. Numerous studies showed that repeated bending of
                                    the stem triggers an increase in stem diameter growth and anatomical changes in internal
                                    stem tissues, affecting especially the development of secondary tissues [55,56,61]. However,
                                    studying the spatio-temporal responses in vivo in the tissues of a secondary-growing
                                    stem is complex and molecular studies seeking to reveal the mechanisms underlying
                                    this acclimation response to external mechanical stimuli are underdeveloped. In poplar,
                                    Pomiès et al. [132] showed that the stem transcriptome is massively remodeled in response
                                    to a single transient-bending stimulus. A total of 2663 genes, representing 6% of the genome,
                                    were found to be regulated after bending, with a large proportion (75%) of these genes being
                                    regulated within the first 2 h after bending. Short-term transcriptomic responses entailed a
                                    rapid stimulation of plant defense and abiotic stress signaling pathways, including ethylene
                                    and jasmonic acid signaling [132]. Late transcriptomic responses affected genes involved
                                    in cell wall organization and/or wood development. By studying more specifically, the
                                    stretched and compressed zones of the bent stem, Roignant et al. [56] demonstrated that
                                    some genes (e.g., MYB69 transcription factor, microtubule-associated protein encoding gene
                                    MAP70) were regulated in the same way in both zones, while FLA genes, encoding fasciclin-
                                    like arabinogalactan proteins known to accumulate during tension wood formation, were
                                    specifically expressed in the stretched zone. These data suggest that cells sense differentially
                                    stretch and compression induced by stem bending. To date, the role of MS channels in this
                                    type of response has not been studied. However, the growth and anatomical differences
                                    that have been established show that this sensitivity to bending modifies the cambial
                                    activity within the stem. Are all living cells in the stem mechanosensitive or is the sensing
                                    localized and secondary signals are transmitted remotely to the cambium?
                                          As in the case of the root, we took advantage of recent RNA-seq data on single cells or
                                    isolated tissues to compare the expression of the MCA, Piezo and OSCA genes. As shown in
                                    Figure 5, AtOSCA4.1, AtOSCA2.5 and AtMCA2 are very weakly expressed in the Arabidopsis
                                    stem. Within the OSCA family, no clade-specific expression pattern emerges from these
                                    data. Whatever the tissue analyzed, the expression of some AtOSCA genes is higher than
                                    Piezo or AtMCA1. In particular, AtOSCA1.3 and AtOSCA3.1 are highly expressed. While
                                    AtPiezo shows a homogeneous expression profile in the different stem tissues, AtOSCA 3.1,
                                    1.3 and 2.2 have particular expression patterns with a very high level in the endodermis and
                                    the differentiating vessel elements. Interestingly, AtMCA1 is expressed more strongly in the
                                    differentiating vessel elements than in the endodermis, a tissue involved in graviperception,
                                    while recent studies showed a role of this channel in hypergravity [104].
                                          In order to investigate whether these tissue-specific expression patterns are found
                                    in other plant species, we also performed data mining and visualization on expression
                                    data obtained by RNA-seq after cryodissection of stem sections at the level of phloem
                                    and differentiating xylem tissues in Populus tremula [129]. As in Arabidopsis, PtPiezo1
                                    shows a homogeneous expression pattern in the different tissues (Figure 6). No data
                                    were found for the PtPiezo2 and PtOSCA2.1 genes, and the level of PtOSCA1.4 and 1.5
                                    expression is very low compared to the other genes. Among the genes encoding MS
                                    channels, PtMCA1 is the most strongly expressed in the regions of expanding xylem and
                                    secondary wall development, whereas PtMCA2 is very weakly expressed in these same
                                    regions. As in Arabidopsis, in the OSCA multigene family, the PtOSCA3.1 isoform has
                                    the highest level of expression in the stem, but with a lower level in xylem cells during
                                    secondary wall differentiation. In clade 2, the genes are homogeneously expressed in all
                                    tissues except PtaOSCA2.5, for which the expression level is very low during the secondary
                                    wall differentiation phase. Finally, heterogeneous expression profiles are observed within
                                    clade 1 of the OSCA family: isoforms 1.1 and 1.2 show a peak of expression in the secondary
                                    wall formation zone while isoforms 1.3 and 1.7 in the phloem and isoforms 1.8 and 1.7
                                    are more strongly expressed in the expanding xylem. Similarly, a peak of expression is
                                    detected for PtOSCA1.9 in mature xylem cells. Note that no cambium-specific expression
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                                                 15 of 27




                                           profile is observed for any of these genes. This study reveals more disparate expression
                                           levels between genes in the xylem expansion zone in poplar. It is interesting to note that in
                                           Arabidopsis, some genes also have a very specific expression profile in the differentiating
                                           xylem vessels.


        OSCA1.1         OSCA1.2                  *
                                           OSCA1.3         OSCA1.4*                           OSCA 2.1 *                    OSCA2.2 *                  OSCA2.3

                                   *                       OSCA1.8*
                                                                                              OSCA2.4                       OSCA2.5
        OSCA1.5         OSCA1.6            OSCA1.7
                                                                                                                    FIBERS
                                 FIBERS                                                                          1200
                             10000
                                                                                                                 1000
                                                                                                                                            Differenciating vessels
                              1000                    Differenciating vessels               Epiderm               800
            Epiderm                                                                                                                                elements
                                                             elements                                             600
                               100
                                                                                                                  400
                                10                                                                                200
                                                                                                                    0
                                   1                                                                                                            Differentiating xylem
                                                          Differentiating xylem      Endoderm                                                    cells and proximal
      Endoderm                                             cells and proximal                                                                       cambium cells
                                                              cambium cells

                                                                                                                                    Differentiating phloem
                                              Differentiating phloem                 Differentiated phloem
     Differentiated phloem                                                                                                              cells and distal
                                                  cells and distal                            cells
              cells                                                                                                                      cambium cells
                                                   cambium cells

                                                                                                                             *
                            OSCA3.1    *    OSCA4.1  *                                               PIEZO             MCA 1 *          MCA 2
                               FIBERS                                                                              FIBERS
                            4000                                                                                1200
                            3000                                                                                1000
                                                  Differenciating vessels                                                               Differenciating vessels
           Epiderm                                                                           Epiderm             800
                                                         elements                                                                              elements
                            2000                                                                                 600
                                                                                                                 400
                            1000
                                                                                                                 200
                               0                      Differentiating xylem                                        0
                                                                                                                                            Differentiating xylem cells
     Endoderm                                          cells and proximal              Endoderm                                              and proximal cambium
                                                          cambium cells                                                                                cells


                                            Differentiating phloem                                                                Differentiating phloem
    Differentiated phloem                                                         Differentiated phloem cells                    cells and distal cambium
                                                cells and distal
             cells                                                                                                                          cells
                                                 cambium cells

      Figure 5. Expression patterns of MCA, Piezo and OSCA genes in different tissues of Arabidopsis mature inflorescence
      stem. Data were retrieved from the tissue-specific transcriptome study of the mature inflorescence stem of Arabidopsis
      thaliana [128] realized by analyzing mRNA from specifically labeled- nuclei covering a comprehensive set of distinct
      tissues (FANS/RNA-seq). Data are available at https://arabidopsis-stem.cos.uni-heidelberg.de (accessed on 20 June 2021).
      The values of expression levels (0 to 10,000) correspond to the mean of normalized read count values (by DESeq2). n = 3 for
      each population. * indicates a p-value < 0.01 in a Likelihood Ratio Test (LRT) results (by DESeq2) testing if genes have
      similar expression among the seven different tissues. See Appendix B.2 for details.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                    16 of 27




                                    14
                                                    i        ii             iii          iv
                                                                                                    PtaOSCA1.1
                                                                                                    PtaOSCA1.2
                                    12
                                                                                                    PtaOSCA1.3
                                    10                                                              PtaOSCA1.4
                                                                                                    PtaOSCA1.5
                                    8                                                               PtaOSCA1.6
                                    6                                                               PtaOSCA1.7
                                                                                                    PtaOSCA1.8
                                    4                                                               PtaOSCA1.9

                                    2

                                    0

                                    14                                                              PtaOSCA2.2
                                    12                                                              PtaOSCA2.3
                                                                                                    PtaOSCA2.4
                                    10                                                              PtaOSCA2.5
                                    8

                                    6
                                    4
                                    2
                                    0

                                    14                                                              PtaOSCA3.1
                                    12                                                              PtaOSCA4.1
                                                                                                    PtaOSCA4.2
                                    10
                                    8

                                    6
                                    4
                                    2
                                    0

                                    14                                                              PtaPIEZO1
                                    12                                                              PtaMCA1.1
                                                                                                    PtaMCA1.2
                                    10
                                    8

                                    6
                                    4
                                    2
                                    0
                                           1       3   5   7   9   1   3   5   7   9   1   3    5
                                         -0      -0 1-0 1-0 1-0 1-1 1-1 1-1 1-1 1-1 1-2 1-2 1-2
                                    T1         T1    T   T   T   T   T   T   T   T   T   T   T

                                    Figure 6. Expression patterns of MCA, Piezo and OSCA genes in the wood-forming tis-
                                    sues of a wild-growing aspen genotype (Populus tremula). Data were retrieved from Sundell
                                    et al. ([129]; Supplementary Dataset 2). Pooled longitudinal tangential cryosections were used to
                                    obtain a continuous sequence of samples extending from differentiated phloem to mature xylem,
                                    with values of expression levels ranging from 0 to 16 (see Appendix B.3 for details). To better
                                    illustrate the location of the different tangential cryosections pooled to produce an RNA-seq sam-
                                    ple, we showed the transverse cross-section image from the sampled tree T1 from ([129], Figure 1).
                                    The pooled samples are visualized by overlaying them on the transverse cross-section and are
                                    grouped into four clusters (from i to iv). These clusters separate key reprogramming events repre-
                                    sented by the dashed lines: (i/ii) occurs between phloem and xylem differentiation, in the middle of
                                    the dividing cambial cells; (ii/iii) marks the end of cell expansion and the onset of secondary cell wall
                                    formation; (iii/iv) marks the end of secondary cell wall deposition and the late maturation of xylem
                                    cells. The cambium zone is located in cryosections T1-04, T1-05 and T1-06.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                            17 of 27




                                    4. Conclusions
                                    4.1. Unraveling the Functions of Mechanosensitive Channels
                                          Although major advances have been made in recent years demonstrating the essential
                                    role of mechanical stresses during a plant’s life cycle, how cells perceive these signals
                                    and which signaling pathways trigger the physiological or developmental responses are
                                    questions that still require exciting research. While the dwarfing phenotype of fer loss-of-
                                    function mutants made it possible to establish the link between these proteins, cell growth
                                    and/or maintenance of cell wall integrity, no particular phenotype has been reported
                                    yet, for example, in the piezo loss-of-function mutants under normal growth conditions.
                                    More careful investigation, possibly under stressful conditions, could reveal the altered
                                    phenotype at either the macroscopic or molecular level. In this respect, the progress made
                                    in transcriptomic studies within a cell type opens new perspectives. Indeed, knowing
                                    in which tissue an MS channel gene is specifically expressed could allow a more specific
                                    targeting of the analysis of this tissue in KO-mutants to detect phenotypes. A further option
                                    could even be to modify the expression of the MS gene specifically in this tissue.
                                          The creation of plants simultaneously mutated for several of these channels in the
                                    same tissue should also be tested to see if these proteins have redundant functions. This
                                    type of approach would be particularly interesting in the case of the multigenic OSCA
                                    family comprising a large number of genes. However, the immense number of possible
                                    combinations makes a systematic exploration of multiple mutants extremely laborious (for
                                    instance, there are 6188 possible quintuple KO-mutants with the 17 OSCA genes of Populus
                                    trichocarpa). Correlations in the tissue-specific expression of MS channel genes could be used
                                    as criteria to narrow down the candidates and focus on the most promising combinations.
                                          Finally, the respective importance of these channels during mechanosensing would
                                    require the ability to correlate their activation with the magnitude of membrane tension.
                                    In this context, pioneer studies using fluorescent nano-probe reporters of membrane tension
                                    are very promising [133].

                                    4.2. Transcriptional Regulation of Mechanosensitive Channel Genes Following a Mechanical Stress
                                          In addition to the tissue-specific expressions shown here, the transcriptional regulation
                                    of the MS channel genes has been poorly studied. Some results suggest that mechanical
                                    stress stimulates the transcription of these genes. For example, Mousavi et al. [111] showed
                                    that Arabidopsis thaliana seedlings grown inside the Murashige and Skoog medium show
                                    a threefold higher expression of AtPiezo in the upper root and root cap than seedlings
                                    grown on the top of this medium. Zhang et al. [113] observed that the inoculation of a
                                    virus led to a significant increase in the expression of AtPiezo in petioles. In the carnivorous
                                    plant Venus flytrap, a transcriptomic study revealed that two MSL genes and an OSCA
                                    gene are upregulated in the touch-sensitive trigger hair following touch [126]. Arabidopsis
                                    thaliana seedlings under hypergravity conditions show upregulation of AtMCA1 and
                                    AtMCA2 in the hypocotyl compared to seedlings under the 1g condition [104]. Since
                                    those mechanics-related gene expression patterns can suggest a gene function in the
                                    mecanosensing pathways, it could be interesting to reproduce our data-mining approach
                                    on previous transcriptome data obtained after a mechanical stress such as those performed
                                    after a transient stem/shoot bending [132,134], after a load has been placed on a tree
                                    stem [135] or after touching rosette leaves [136]. The expression dynamics of MS channel
                                    genes would probably give precious insight into their role in the physiological response,
                                    in short and long term. This kind of approach, combining mining and visualization of large
                                    molecular datasets with mechanical analyses at the tissue level, is a good illustration of the
                                    flourishing field of quantitative plant biology [137].
                                          If the transcriptional regulation of MS channel genes after mechanical stress is to be
                                    confirmed, what are the implications for the amount of these proteins in the membranes?
                                    Is the transcriptional regulation just a way to maintain a constant concentration of MS
                                    channels, or could it modulate the mechanosensitivity of stimulated tissues?
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                 18 of 27




                                    4.3. Practical Applications of Thigmomorphogenesis
                                          The ability of plants to respond to mechanical stress is more than a theoretical curiosity.
                                    For centuries, Japanese farmers have taken advantage of this phenomenon in a practice
                                    called “mugifumi”, which consists in treading young wheat or barley plants to reduce the
                                    risk of lodging and increase yield [138]. This practical application of thigmomorphogenesis
                                    avant la lettre is bound to generalize and diversify as environmentally-friendly substitutes
                                    for current chemical treatments. For instance, mechanostimulating garden roses under
                                    greenhouse conditions increases branching and compactness [139], and could become
                                    an alternative to hormonal treatments in horticulture. In Poaceae, exposure to wind
                                    and imposed flexure have an impact on agronomic traits [140]. Furthermore, as several
                                    studies showed that various forms of mechanical stimuli enhanced plants’ basal defense
                                    responses (see [141] for a review), mechanostimulation could be a potential priming method
                                    for sustainable agriculture, alternative to chemical-based priming. Developing efficient
                                    applications requires new phenotyping techniques for measuring mechanical traits such as
                                    the resistance to lodging [142], but also a deeper understanding of the actors involved in
                                    the mechanosensing pathways.
                                          The relevance of thigmomorphogenesis to tree growth in non-controlled conditions [60]
                                    also opens new avenues for forest management, especially given the current increase in
                                    frequency of extreme windstorms [143]. At the macroscopic level, the functional biome-
                                    chanical traits quantifying the strength and safety of trees against wind and self-buckling
                                    are well-established [144]. Trees acclimate to their mechanical environment by constantly
                                    adjusting these traits thanks to mechanosensing. However, the molecular actors involved
                                    in this feedback loop are largely unknown. Indeed, while many molecular studies have
                                    focused on the outermost tissues of organs (root cap, epidermis of the shoot apical meris-
                                    tem), few studies targeted the xylem, phloem or endodermis of stems, even though some
                                    of the MS channels genes are highly expressed in these tissues. The difficulty of performing
                                    in vivo spatio-temporal analyses in secondary tissues partly explains this lack of data.
                                    A future solution could be experimental setups for growing cambium in vitro, mimicking
                                    the mechanical and hormonal environment of the cambium in trees. In any case, perennial
                                    plants are the systems in which investigating the localization and functions of MS channels
                                    is the most ecologically relevant.

                                    Supplementary Materials: The following are available online at https://www.mdpi.com/article/10
                                    .3390/ijms222011043/s1.
                                    Author Contributions: Conceptualization, F.P.H., E.T. and N.L.-F.; methodology, F.P.H., E.T. and
                                    N.L.-F.; software, F.P.H.; formal analysis, E.T. and N.L.-F.; investigation, F.P.H., E.T. and N.L.-F.;
                                    writing—original draft preparation, F.P.H., E.T. and N.L.-F.; writing—review and editing, J.-L.J.;
                                    visualization, F.P.H., E.T. and N.L.-F. All authors have read and agreed to the published version of
                                    the manuscript.
                                    Funding: This work was funded by the I-SITE CAP 20-25 (ANR grant 16-IDEX-0001) Emergence
                                    2019 from the University of Clermont-Auvergne, France. Erwan Tinturier benefits from a PhD grant
                                    funded by the French Ministry of Higher Education, Research and Innovation. Funding bodies were
                                    not implied in the design and analysis of the study.
                                    Data Availability Statement: Expression patterns of MCA, Piezo and OSCA genes were retrieved
                                    from the BAR ePlantArabidospsis website (https://bar.utoronto.ca/eplant (accessed on 23 February
                                    2021) for the Arabidopsis root, from https://arabidopsis-stem.cos.uni-heidelberg.de (accessed on 20
                                    June 2021) for the Arabidopsis mature inflorescence stem, and from http://aspwood.popgenie.org
                                    (accessed on 20 June 2021) for wood-forming tissues in Populus tremula.
                                    Acknowledgments: We thank Mélanie Decourteix, Jean-Stéphane Venisse and Marylou Mantova for
                                    advice on phylogenetic trees, and Valérie Legué for comments on the manuscript.
                                    Conflicts of Interest: The authors declare no conflict of interest.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                            19 of 27




                                    Appendix A. Phylogeny
                                          Coding sequences for Piezo, MCA and OSCA families were isolated using TBLASTX
                                    searches (Phytozome v12.1), in which Arabidopsis thaliana family members were used
                                    as query sequences against the coding sequences of Populus trichocarpa V3.0. Sequence
                                    alignments were generated using MAFFT version 7 with auto-option [145]. Maximum-
                                    likelihood trees were reconstructed from translated protein sequences using MEGA with
                                    an LG substitution model. Bootstrapping with 1000 replicates was performed to evaluate
                                    the credibility of tree topology. MCA and OSCA unrooted trees were obtained. The Piezo
                                    unrooted tree was obtained without bootstrap because it contained only three sequences.
                                          The three illustrations of the tree of life in Figure 2 were based on the taxonomy of the
                                    National Center for Biotechnology Information, with simplifications for the sake of clarity.

                                    Appendix B. Tissue-Specific Expression Data
                                    Appendix B.1. Data from Single-Cell RNA-seq of Tissue/Cell-Types from Arabidopsis Roots
                                          Biological data were retrieved from a single-cell RNA-sequencing (scRNA-seq) ex-
                                    periment performed by Ryu et al. [127] from protoplasts of more than 10,000 Arabidopsis
                                    root cells issued of 5-day-old seedlings primary root tips. ScRNA-seq was performed
                                    using commercially available droplet-based microfluidics. The authors obtained a to-
                                    tal of 7522 single-cell transcriptomes from three biological replicates of protoplasts from
                                    wild-type (Columbia ecotype) Arabidopsis root tips. Approximately 75,000 reads were
                                    obtained per cell, which generated a median of 24,000 unique molecular identifiers per
                                    cell, 5000 expressed genes per cell, and more than 22,000 total genes detected in the popu-
                                    lation. An unsupervised clustering was performed on, using Seurat, which yielded nine
                                    major clusters of cell transcriptomes. To enable tissue/cell type assignment to particular
                                    clusters, the authors used the analysis of differentially expressed genes, gene ontology
                                    and the analysis of transcript accumulation of 86 marker genes known to be preferentially
                                    expressed in particular root tissue/cell types. Each dataset was log-normalized, scaled,
                                    and corrected for dataset-specific batch effects using ComBat (sva v3.26.00; [146]). In their
                                    article, the authors represent their data usually by plotting the single-cell transcriptomes
                                    via t-distributed stochastic neighbor embedding (tSNE) projection. This yielded largely
                                    overlapping distributions of cells from each of the biological replicates, indicating a high
                                    degree of reproducibility.
                                          For the construction of our Figure 4 and Appendix B.1, the data for each gene were
                                    retrieved from the BAR ePlantArabidospsis website available at https://bar.utoronto.ca/
                                    eplant (accessed on 23 February 2021). For example, to retrieve data for AtOSCA1.1, we
                                    entered its accession number AT4G04340 in the search bar (see Table S1 for the relationships
                                    between gene names and accession numbers), then clicked on Tissue and Experiment eFP
                                    viewers, then on Single Cell eFP (RNA-Seq data). The resulting view can be accessed directly
                                    from the URL https://bar.utoronto.ca/eplant/?ActiveSpecies=Arabidopsis%20thaliana&
                                    Genes=AT4G04340&ActiveGene=AT4G04340&ActiveView=SingleCellView (accessed on
                                    23 February 2021). The raw data were then downloaded as JSON files.
                                          For the different tissue/cell types, to facilitate the graphical representation of expres-
                                    sion levels in tissues, only expression values from sub-clusters containing differentiated
                                    (not differentiating) cells were used. In the stele, only the expression data from xylem- and
                                    phloem-cell types are shown. In the meristematic zone, we represented the expression
                                    mean of dividing cells and cells from the quiescent center.
Int. J. Mol. Sci. 2021, 22, 11043                                                                                               20 of 27




                                                                                          AtMCA1            AtMCA2
                                        pericycle      phloem   xylem
                                     endodermis
                                          cortex                             root hair
                                       epidermis
                                                                        meristematic
                                             lateral                       zone
                                            root cap

                                                                columella


                                           AtOSCA1.1              AtOSCA1.2              AtOSCA1.3         AtOSCA1.4




                                                                                                                                  0.8



                                                                                                                                  0.7


                                           AtOSCA1.5              AtOSCA1.6              AtOSCA1.7         AtOSCA1.8              0.6



                                                                                                                                  0.5



                                                                                                                                  0.4



                                                                                                                                  0.3
                                           AtOSCA2.1              AtOSCA2.2              AtOSCA2.3         AtOSCA2.4

                                                                                                                                  0.2



                                                                                                                                  0.1



                                                                                                                                  0.0


                                           AtOSCA2.5              AtOSCA3.1              AtOSCA4.1         AtPiezo1




                                    Figure A1. Expression patterns of MCA, Piezo and OSCA genes in different tissues of the Arabidopsis
                                    root using a common scale. Unlike Figure 4, which shows an individual scale for each gene, this
                                    figure allows comparisons between expression levels of different genes.

                                    Appendix B.2. RNA-seq Experiments from Nuclei of Different Cell-Types in Mature Inflorescence
                                    Stem of Arabidopsis thaliana
                                         To distinguish between the different cell types in mature inflorescence stems of Ara-
                                    bidopsis, Shi et al. [128] produced transgenic Arabidospsis plants transformed with construc-
                                    tion containing tissue-specific promoters controlling the expression of the GFP fluorescent
                                    reporter. The different promoter chosen by the authors were: the NAC SECONDARY
Int. J. Mol. Sci. 2021, 22, 11043                                                                                            21 of 27




                                    WALL THICKENING PROMOTING3 (NST3) promoter to label fibers; the VASCULAR-
                                    RELATED NAC DOMAIN PROTEIN7 (VND7) promoter for differentiating vessel elements;
                                    the PHLOEM INTERCALATED WITH XYLEM (PXY)/TDIF RECEPTOR (TDR) promoter
                                    for differentiating xylem cells and proximal cambium cells; the SMAX1-LIKE5 (SMXL5)
                                    promoter for differentiating phloem cells and distal cambium cells; the ALTERED PHLOEM
                                    DEVELOPMENT (APL) promoter for differentiated phloem cells; the SCARECROW (SCR)
                                    promoter for starch sheath cells; and the LIPID TRANSFER PROTEIN1 (LTP1) promoter
                                    for epidermis cells. The nuclei were isolated from the second internodes of Arabidopsis
                                    inflorescence stems. By combining fluorescence-activated nucleus sorting and laser-capture
                                    microdissection with next-generation RNA sequencing, the authors characterized and
                                    classified more than 15,000 genes as being differentially expressed in xylem vessels, fibers,
                                    the proximal and distal cambium, phloem, phloem cap, pith, starch sheath, and epider-
                                    mis cells.
                                          To prepare the spider-graphs in Figure 5, tissue-specific gene expression values were
                                    retrieved from https://arabidopsis-stem.cos.uni-heidelberg.de (accessed on 20 June 2021)
                                    by successively entering the accession numbers of MS genes into the search bar. We
                                    computed the average expression levels of the three biological replicates.

                                    Appendix B.3. RNA-seq Experiments from Cryosections Spanning the Secondary Phloem, Vascular
                                    Cambium, and Wood-Forming Tissues of Populus tremula
                                         Biological data were retrieved from the RNA-seq experiment performed by
                                    Sundell et al. ([129], Supplementary Dataset 2) and also available on the interactive web re-
                                    source http://aspwood.popgenie.org (accessed on 20 June 2021). In this study, the authors
                                    collected and cut longitudinal tangential cryosections (15 µm thick) using a cryo-microtome
                                    in the stem zone covering the entire current-year radial growth zone of poplar trees. The to-
                                    tal number of sections varied from 105 to 135 in the four different 45-year old aspen trees
                                    sampled during the middle of the growing season. For RNA-seq experiments, these sec-
                                    tions were pooled into 25 to 28 samples for each replicate tree, thanks to images taken
                                    with a light microscope during the process of sectioning. The pooling was based on the
                                    estimated tissue composition from anatomical inspection. Details of the composition of
                                    the 25 samples are given in ([129], Supplementary Dataset 1). After RNA-seq, the val-
                                    ues of expression levels were estimated after normalization of the read counts using a
                                    variance-stabilizing transformation as implemented in DESeq [129].
                                         To prepare the Figure 6, we retrieved data directly from the Supplementary Dataset 2
                                    of [129], which is a Microsoft Excel file. To simplify the illustration of expression profiles
                                    (the number of sections composing the 4 clusters can be separated from several sections
                                    between the 4 tree replicates), we showed only the results obtained on the sampled tree
                                    T1 since similar expression profiles are obtained when the three other samples trees are
                                    analyzed. By a hierarchical clustering from mRNA expression values for all expressed
                                    genes, Sundell et al. [129] identified four sample clusters of expression. The authors
                                    describe that these gene expression clusters were found to separate key reprogramming
                                    events: (i/ii) occurs between phloem and xylem differentiation, in the middle of the dividing
                                    cambial cells; (ii/iii) marks the end of cell expansion and the onset of secondary cell wall
                                    formation; (iii/iv) marks the end of secondary cell wall deposition and the late maturation
                                    of xylem cells.

References
1.    Moulia, B.; Coutand, C.; Julien, J.L. Mechanosensitive control of plant growth: Bearing the load, sensing, transducing and
      responding. Front. Plant Sci. 2015, 6, 52. [CrossRef]
2.    Gardiner, B.; Berry, P.; Moulia, B. Review: Wind impacts on plant growth, mechanics and damage. Plant Sci. 2016, 245, 94–118.
      [CrossRef]
3.    Alméras, T.; Gril, J.; Costes, E. Bending of apricot-tree branches under the weight of axillary productions: confrontation of a
      mechanical model to experimental data. Trees 2002, 16, 5–15. [CrossRef]
4.    Moulia, B.; Bastien, R.; Chauvet-Thiry, H.; Leblanc-Fournier, N. Posture control in land plants: growth, position sensing,
      proprioception, balance, and elasticity. J. Exp. Bot. 2019, 70, 3467–3494. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                    22 of 27




5.    Kolb, E.; Legué, V.; Bogeat-Triboulot, M.B. Physical root-soil interactions. Phys. Biol. 2017, 14, 065004. [CrossRef] [PubMed]
6.    Puijalon, S.; Bouma, T.J.; Douady, C.J.; van Groenendael, J.; Anten, N.P.R.; Martel, E.; Bornette, G. Plant resistance to mechanical
      stress: evidence of an avoidance–tolerance trade-off. New Phytol. 2011, 191, 1141–1149. [CrossRef] [PubMed]
7.    Denny, M.; Gaylord, B. The mechanics of wave-swept algae. J. Exp. Biol. 2002, 205, 1355–1362. [CrossRef] [PubMed]
8.    Green, P.B. Mechanism for plant cellular morphogenesis. Science 1962, 138, 1404–1405. [CrossRef]
9.    Lockhart, J.A. An analysis of irreversible plant cell elongation. J. Theor. Biol. 1965, 8, 264–275. [CrossRef]
10.   Weber, A.; Braybrook, S.; Huflejt, M.; Mosca, G.; Routier-Kierzkowska, A.L.; Smith, R.S. Measuring the mechanical properties of
      plant cells by combining micro-indentation with osmotic treatments. J. Exp. Bot. 2015, 66, 3229–3241. [CrossRef]
11.   Mosca, G.; Sapala, A.; Strauss, S.; Routier-Kierzkowska, A.L.; Smith, R.S. On the micro-indentation of plant cells in a tissue
      context. Phys. Biol. 2017, 14, 015003. [CrossRef]
12.   Sampathkumar, A.; Krupinski, P.; Wightman, R.; Milani, P.; Berquand, A.; Boudaoud, A.; Hamant, O.; Jönsson, H.; Meyerowitz,
      E.M. Subcellular and supracellular mechanical stress prescribes cytoskeleton behavior in Arabidopsis cotyledon pavement cells.
      eLife 2014, 3, e01967. [CrossRef] [PubMed]
13.   Sapala, A.; Runions, A.; Routier-Kierzkowska, A.L.; Gupta, M.D.; Hong, L.; Hofhuis, H.; Verger, S.; Mosca, G.; Li, C.B.; Hay, A.;
      et al. Why plants make puzzle cells, and how their shape emerges. eLife 2018, 7, e32794. [CrossRef] [PubMed]
14.   Kierzkowski, D.; Routier-Kierzkowska, A.L. Cellular basis of growth in plants: geometry matters. Curr. Opin. Plant Biol. 2019,
      47, 56–63. [CrossRef] [PubMed]
15.   Long, Y.; Cheddadi, I.; Mosca, G.; Mirabet, V.; Dumond, M.; Kiss, A.; Traas, J.; Godin, C.; Boudaoud, A. Cellular heterogeneity in
      pressure and growth emerges from tissue topology and geometry. Curr. Biol. 2020, 30, 1504–1516.e8. [CrossRef]
16.   Verger, S.; Long, Y.; Boudaoud, A.; Hamant, O. A tension-adhesion feedback loop in plant epidermis. eLife 2018, 7, e34460.
      [CrossRef]
17.   Hejnowicz, Z. Graviresponses in herbs and trees: a major role for the redistribution of tissue and growth stresses. Planta 1997,
      203, S136–S146. [CrossRef]
18.   Vandiver, R.; Goriely, A. Tissue tension and axial growth of cylindrical structures in plants and elastic tissues. EPL Europhys. Lett.
      2008, 84, 58004. [CrossRef]
19.   Moulia, B.; Fournier, M. The power and control of gravitropic movements in plants: A biomechanical and systems biology view.
      J. Exp. Bot. 2009, 60, 461–486. [CrossRef]
20.   Moulia, B. Plant biomechanics and mechanobiology are convergent paths to flourishing interdisciplinary research. J. Exp. Bot.
      2013, 64, 4617–4633. [CrossRef]
21.   Kierzkowski, D.; Nakayama, N.; Routier-Kierzkowska, A.L.; Weber, A.; Bayer, E.; Schorderet, M.; Reinhardt, D.; Kuhlemeier, C.;
      Smith, R.S. Elastic domains regulate growth and organogenesis in the plant shoot apical meristem. Science 2012, 335, 1096–1099.
      [CrossRef]
22.   Hamant, O.; Heisler, M.G.; Jönsson, H.; Krupinski, P.; Uyttewaal, M.; Bokov, P.; Corson, F.; Sahlin, P.; Boudaoud, A.; Meyerowitz,
      E.M.; et al. Developmental patterning by mechanical signals in Arabidopsis. Science 2008, 322, 1650–1655. [CrossRef]
23.   Beauzamy, L.; Louveaux, M.; Hamant, O.; Boudaoud, A. Mechanically, the shoot apical meristem of Arabidopsis behaves like a
      shell inflated by a pressure of about 1 MPa. Front. Plant Sci. 2015, 6, 1038. [CrossRef]
24.   Hejnowicz, Z.; Sievers, A. Tissue stresses in organs of herbaceous plants: II. Determination in three dimensions in the hypocotyl
      of sunflower. J. Exp. Bot. 1995, 46, 1045–1053. [CrossRef]
25.   Kutschera, U.; Niklas, K.J. The epidermal-growth-control theory of stem elongation: An old and a new perspective. J. Plant
      Physiol. 2007, 164, 1395–1409. [CrossRef] [PubMed]
26.   Archer, R.R. Growth Stresses and Strains in Trees; Springer: Berlin, Germany, 1987.
27.   Alméras, T.; Clair, B. Critical review on the mechanisms of maturation stress generation in trees. J. R. Soc. Interface 2016,
      13, 20160550. [CrossRef] [PubMed]
28.   Alméras, T.; Fournier, M. Biomechanical design and long-term stability of trees: Morphological and wood traits involved in the
      balance between weight increase and the gravitropic reaction. J. Theor. Biol. 2009, 256, 370–381. [CrossRef] [PubMed]
29.   Clair, B.; Ghislain, B.; Prunier, J.; Lehnebach, R.; Beauchêne, J.; Alméras, T. Mechanical contribution of secondary phloem to
      postural control in trees: The bark side of the force. New Phytol. 2018, 221, 209–217. [CrossRef] [PubMed]
30.   Telewski, F.W. A unified hypothesis of mechanoperception in plants. Am. J. Bot. 2006, 93, 1466–1476. [CrossRef] [PubMed]
31.   Bidhendi, A.J.; Altartouri, B.; Gosselin, F.P.; Geitmann, A. Mechanical stress initiates and sustains the morphogenesis of wavy leaf
      epidermal cells. Cell Rep. 2019, 28, 1237–1250.e6. [CrossRef]
32.   Reinhardt, D.; Pesce, E.R.; Stieger, P.; Mandel, T.; Baltensperger, K.; Bennett, M.; Traas, J.; Friml, J.; Kuhlemeier, C. Regulation of
      phyllotaxis by polar auxin transport. Nature 2003, 426, 255–260. [CrossRef]
33.   Smith, R.S.; Guyomarc’h, S.; Mandel, T.; Reinhardt, D.; Kuhlemeier, C.; Prusinkiewicz, P. A plausible model of phyllotaxis. Proc.
      Natl. Acad. Sci. USA 2006, 103, 1301–1306. [CrossRef]
34.   Bayer, E.M.; Smith, R.S.; Mandel, T.; Nakayama, N.; Sauer, M.; Prusinkiewicz, P.; Kuhlemeier, C. Integration of transport-based
      models for phyllotaxis and midvein formation. Genes Dev. 2009, 23, 373–384. [CrossRef] [PubMed]
35.   Hartmann, F.P.; Barbier de Reuille, P.; Kuhlemeier, C. Toward a 3D model of phyllotaxis based on a biochemically plausible
      auxin-transport mechanism. PLoS Comput. Biol. 2019, 15, e1006896. [CrossRef] [PubMed]
36.   Arsuffi, G.; Braybrook, S.A. Acid growth: An ongoing trip. J. Exp. Bot. 2018, 69, 137–146. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                       23 of 27




37.   Heisler, M.G.; Hamant, O.; Krupinski, P.; Uyttewaal, M.; Ohno, C.; Jönsson, H.; Traas, J.; Meyerowitz, E.M. Alignment between
      PIN1 polarity and microtubule orientation in the shoot apical meristem reveals a tight coupling between morphogenesis and
      auxin transport. PLoS Biol. 2010, 8, e1000516. [CrossRef]
38.   Nakayama, N.; Smith, R.; Mandel, T.; Robinson, S.; Kimura, S.; Boudaoud, A.; Kuhlemeier, C. Mechanical regulation of
      auxin-mediated growth. Curr. Biol. 2012, 22, 1468–1476. [CrossRef]
39.   Landrein, B.; Kiss, A.; Sassi, M.; Chauvet, A.; Das, P.; Cortizo, M.; Laufs, P.; Takeda, S.; Aida, M.; Traas, J.; et al. Mechanical stress
      contributes to the expression of the STM homeobox gene in Arabidopsis shoot meristems. eLife 2015, 4, e07811. [CrossRef]
40.   Hejnowicz, Z.; Rusin, A.; Rusin, T. Tensile tissue stress affects the orientation of cortical microtubules in the epidermis of
      sunflower hypocotyl. J. Plant Growth Regul. 2000, 19, 31–44. [CrossRef]
41.   Robinson, S.; Kuhlemeier, C. Global compression reorients cortical microtubules in Arabidopsis hypocotyl epidermis and promotes
      growth. Curr. Biol. 2018, 28, 1794–1802.e2. [CrossRef]
42.   Burian, A.; Ludynia, M.; Uyttewaal, M.; Traas, J.; Boudaoud, A.; Hamant, O.; Kwiatkowska, D. A correlative microscopy approach
      relates microtubule behaviour, local organ geometry, and cell growth at the Arabidopsis shoot apical meristem. J. Exp. Bot. 2013,
      64, 5753–5767. [CrossRef]
43.   Hamant, O.; Moulia, B. How do plants read their own shapes? New Phytol. 2016, 212, 333–337. [CrossRef]
44.   Kabir, A.M.R.; Inoue, D.; Hamano, Y.; Mayama, H.; Sada, K.; Kakugo, A. Biomolecular motor modulates mechanical property of
      microtubule. Biomacromolecules 2014, 15, 1797–1805. [CrossRef]
45.   Mirabet, V.; Krupinski, P.; Hamant, O.; Meyerowitz, E.M.; Jönsson, H.; Boudaoud, A. The self-organization of plant microtubules
      inside the cell volume yields their cortical localization, stable alignment, and sensitivity to external cues. PLoS Comput. Biol. 2018,
      14, e1006011. [CrossRef]
46.   Hamant, O.; Inoue, D.; Bouchez, D.; Dumais, J.; Mjolsness, E. Are microtubules tension sensors? Nat. Commun. 2019, 10, 1–12.
      [CrossRef] [PubMed]
47.   Paredez, A.R.; Somerville, C.R.; Ehrhardt, D.W. Visualization of cellulose synthase demonstrates functional association with
      microtubules. Science 2006, 312, 1491–1495. [CrossRef] [PubMed]
48.   Hervieux, N.; Dumond, M.; Sapala, A.; Routier-Kierzkowska, A.L.; Kierzkowski, D.; Roeder, A.; Smith, R.; Boudaoud, A.; Hamant,
      O. A mechanical feedback restricts sepal growth and shape in Arabidopsis. Curr. Biol. 2016, 26, 1019–1028. [CrossRef] [PubMed]
49.   Hervieux, N.; Tsugawa, S.; Fruleux, A.; Dumond, M.; Routier-Kierzkowska, A.L.; Komatsuzaki, T.; Boudaoud, A.; Larkin, J.C.;
      Smith, R.S.; Li, C.B.; et al. Mechanical shielding of rapidly growing cells buffers growth heterogeneity and contributes to organ
      shape reproducibility. Curr. Biol. 2017, 27, 3468–3479.e4. [CrossRef]
50.   Stokes, A.; Nicoll, B.C.; Coutts, M.P.; Fitter, A.H. Responses of young Sitka spruce clones to mechanical perturbation and nutrition:
      effects on biomass allocation, root development, and resistance to bending. Can. J. For. Res. 1997, 27, 1049–1057. [CrossRef]
51.   Nicoll, B.C.; Gardiner, B.A.; Peace, A.J. Improvements in anchorage provided by the acclimation of forest trees to wind stress. For.
      Int. J. For. Res. 2008, 81, 389–398. [CrossRef]
52.   Telewski, F.W.; Pruyn, M.L. Thigmomorphogenesis: A dose response to flexing in Ulmus americana seedlings. Tree Physiol. 1998,
      18, 65–68. [CrossRef] [PubMed]
53.   Coutand, C.; Dupraz, C.; Jaouen, G.; Ploquin, S.; Adam, B. Mechanical stimuli regulate the allocation of biomass in trees:
      Demonstration with young Prunus avium trees. Ann. Bot. 2008, 101, 1421–1432. [CrossRef] [PubMed]
54.   Niez, B.; Dlouhá, J.; Moulia, B.; Badel, E. Water-stressed or not, the mechanical acclimation is a priority requirement for trees.
      Trees 2019, 33, 279–291. [CrossRef]
55.   Telewski, F.W. Structure and function of flexure wood in Abies fraseri. Tree Physiol. 1989, 5, 113–121. [CrossRef]
56.   Roignant, J.; Badel, É.; Leblanc-Fournier, N.; Brunel-Michac, N.; Ruelle, J.; Moulia, B.; Decourteix, M. Feeling stretched or
      compressed? The multiple mechanosensitive responses of wood formation to bending. Ann. Bot. 2018, 121, 1151–1161. [CrossRef]
57.   Niez, B.; Dlouhá, J.; Gril, J.; Ruelle, J.; Toussaint, E.; Moulia, B.; Badel, E. Mechanical properties of “flexure wood”: Compressive
      stresses in living trees improve the mechanical resilience of wood and its resistance to damage. Ann. For. Sci. 2020, 77, 17.
      [CrossRef]
58.   Jaffe, M.J. Thigmomorphogenesis: The response of plant growth and development to mechanical stimulation. Planta 1973,
      114, 143–157. [CrossRef]
59.   Fournier, M.; Stokes, A.; Coutand, C.; Fourcaud, T.; Moulia, B. Tree biomechanics and growth strategies in the context of forest
      functional ecology. In Ecology and Biomechanics: A Mechanical Approach to the Ecology of Animals and Plants; CRC Press: Boca Raton,
      FL, USA, 2006; pp. 1–34.
60.   Bonnesoeur, V.; Constant, T.; Moulia, B.; Fournier, M. Forest trees filter chronic wind-signals to acclimate to high winds. New
      Phytol. 2016, 210, 850–860. [CrossRef]
61.   Paul-Victor, C.; Rowe, N. Effect of mechanical perturbation on the biomechanics, primary growth and secondary tissue
      development of inflorescence stems of Arabidopsis thaliana. Ann. Bot. 2010, 107, 209–218. [CrossRef]
62.   Zhdanov, O.; Blatt, M.R.; Zare-Behtash, H.; Busse, A. Wind-evoked anemotropism affects the morphology and mechanical
      properties of Arabidopsis. J. Exp. Bot. 2021, 72, 1906–1918. [CrossRef]
63.   Anten, N.P.R.; Alcalá-Herrera, R.; Schieving, F.; Onoda, Y. Wind and mechanical stimuli differentially affect leaf traits in Plantago
      major. New Phytol. 2010, 188, 554–564. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                     24 of 27




64.   Schoelynck, J.; Puijalon, S.; Meire, P.; Struyf, E. Thigmomorphogenetic responses of an aquatic macrophyte to hydrodynamic
      stress. Front. Plant Sci. 2015, 6, 43. [CrossRef]
65.   Ditengou, F.A.; Teale, W.D.; Kochersperger, P.; Flittner, K.A.; Kneuper, I.; van der Graaff, E.; Nziengui, H.; Pinosa, F.; Li, X.;
      Nitschke, R.; et al. Mechanical induction of lateral root initiation in Arabidopsis thaliana. Proc. Natl. Acad. Sci. USA 2008,
      105, 18818–18823. [CrossRef]
66.   Richter, G.L.; Monshausen, G.B.; Krol, A.; Gilroy, S. Mechanical stimuli modulate lateral root organogenesis. Plant Physiol. 2009,
      151, 1855–1866. [CrossRef]
67.   Monshausen, G.B.; Bibikova, T.N.; Weisenseel, M.H.; Gilroy, S. Ca2+ regulates reactive oxygen species production and pH during
      mechanosensing in Arabidopsis roots. Plant Cell 2009, 21, 2341–2356. [CrossRef]
68.   Bizet, F.; Bengough, A.G.; Hummel, I.; Bogeat-Triboulot, M.B.; Dupuy, L.X. 3D deformation field in growing plant roots reveals
      both mechanical and biological responses to axial mechanical forces. J. Exp. Bot. 2016, 67, 5605–5614. [CrossRef]
69.   Roué, J.; Chauvet, H.; Brunel-Michac, N.; Bizet, F.; Moulia, B.; Badel, E.; Legué, V. Root cap size and shape influence responses
      to the physical strength of the growth medium in Arabidopsis thaliana primary roots. J. Exp. Bot. 2020, 71, 126–137. [CrossRef]
      [PubMed]
70.   Coutand, C.; Julien, J.; Moulia, B.; Mauget, J.; Guitard, D. Biomechanical study of the effect of a controlled bending on tomato
      stem elongation: Global mechanical analysis. J. Exp. Bot. 2000, 51, 1813–1824. [CrossRef] [PubMed]
71.   Moulia, B.; Der Loughian, C.; Bastien, R.; Martin, O.; Rodríguez, M.; Gourcilleau, D.; Barbacci, A.; Badel, E.; Franchel, J.;
      Lenne, C.; et al. Integrative mechanobiology of growth and architectural development in changing mechanical environments.
      In Mechanical Integration of Plant Cells and Plants; Signaling and Communication in Plants; Wojtaszek, P., Ed.; Springer:
      Berlin/Heidelberg, Germany, 2011; Volume 9, pp. 269–302. [CrossRef]
72.   Lopez, R.; Badel, É.; Peraudeau, S.; Leblanc-Fournier, N.; Beaujard, F.; Julien, J.L.; Cochard, H.; Moulia, B. Tree shoot bending
      generates hydraulic pressure pulses: A new long-distance signal? J. Exp. Bot. 2014, 65, 1997–2008. [CrossRef]
73.   Louf, J.F.; Guéna, G.; Badel, E.; Forterre, Y. Universal poroelastic mechanism for hydraulic signals in biomimetic and natural
      branches. Proc. Natl. Acad. Sci. USA 2017, 114, 11034–11039. [CrossRef]
74.   Tinturier, E.; Badel, E.; Leblanc-Fournier, N.; Julien, J.L. Stem bending generates electrical response in poplar. Physiol. Plant. 2021.
      [CrossRef] [PubMed]
75.   Chauvin, A.; Caldelari, D.; Wolfender, J.L.; Farmer, E.E. Four 13-lipoxygenases contribute to rapid jasmonate synthesis in
      wounded Arabidopsis thaliana leaves: A role for lipoxygenase 6 in responses to long-distance wound signals. New Phytol. 2013,
      197, 566–575. [CrossRef] [PubMed]
76.   Chehab, E.; Yao, C.; Henderson, Z.; Kim, S.; Braam, J. Arabidopsis touch-induced morphogenesis is jasmonate mediated and
      protects against pests. Curr. Biol. 2012, 22, 701–706. [CrossRef] [PubMed]
77.   Farmer, E.E.; Gasperini, D.; Acosta, I.F. The squeeze cell hypothesis for the activation of jasmonate synthesis in response to
      wounding. New Phytol. 2014, 204, 282–288. [CrossRef]
78.   Tixier, A.; Badel, E.; Franchel, J.; Lakhal, W.; Leblanc-Fournier, N.; Moulia, B.; Julien, J.L. Growth and molecular responses to
      long-distance stimuli in poplars: Bending vs flame wounding. Physiol. Plant. 2014, 150, 225–237. [CrossRef]
79.   Fal, K.; Korsbo, N.; Alonso-Serra, J.; Teles, J.; Liu, M.; Refahi, Y.; Chabouté, M.E.; Jönsson, H.; Hamant, O. Tissue folding at
      the organ-meristem boundary results in nuclear compression and chromatin compaction. Proc. Natl. Acad. Sci. USA 2021, 118.
      [CrossRef]
80.   Bacete, L.; Hamann, T. The role of mechanoperception in plant cell wall integrity maintenance. Plants 2020, 9, 574. [CrossRef]
81.   Frachisse, J.M.; Thomine, S.; Allain, J.M. Calcium and plasma membrane force-gated ion channels behind development. Curr.
      Opin. Plant Biol. 2020, 53, 57–64. [CrossRef]
82.   Guo, H.; Li, L.; Ye, H.; Yu, X.; Algreen, A.; Yin, Y. Three related receptor-like kinases are required for optimal cell elongation in
      Arabidopsis thaliana. Proc. Natl. Acad. Sci. USA 2009, 106, 7648–7653. [CrossRef] [PubMed]
83.   Shih, H.W.; Miller, N.D.; Dai, C.; Spalding, E.P.; Monshausen, G.B. The receptor-like kinase FERONIA is required for mechanical
      signal transduction in Arabidopsis seedlings. Curr. Biol. 2014, 24, 1887–1892. [CrossRef]
84.   Li, E.; Wang, G.; Zhang, Y.; Kong, Z.; Li, S. FERONIA mediates root nutating growth. Plant J. 2020, 104, 1105–1116. [CrossRef]
85.   Dong, Q.; Zhang, Z.; Liu, Y.; Tao, L.; Liu, H. FERONIA regulates auxin-mediated lateral root development and primary root
      gravitropism. FEBS Lett. 2019, 593, 97–106. [CrossRef] [PubMed]
86.   Wang, K.; Yang, Z.; Qing, D.; Ren, F.; Liu, S.; Zheng, Q.; Liu, J.; Zhang, W.; Dai, C.; Wu, M.; et al. Quantitative and functional
      posttranslational modification proteomics reveals that TREPH1 plays a role in plant touch-delayed bolting. Proc. Natl. Acad. Sci.
      USA 2018, 115, E10265–E10274. [CrossRef]
87.   Hamilton, E.S.; Schlegel, A.M.; Haswell, E.S. United in diversity: Mechanosensitive ion channels in plants. Annu. Rev. Plant Biol.
      2015, 66, 113–137. [CrossRef]
88.   Basu, D.; Haswell, E.S. Plant mechanosensitive ion channels: An ocean of possibilities. Curr. Opin. Plant Biol. 2017, 40, 43–48.
      [CrossRef]
89.   White, P.J.; Broadley, M.R. Calcium in plants. Ann. Bot. 2003, 92, 487–511. [CrossRef]
90.   Knight, M.R.; Smith, S.M.; Trewavas, A.J. Wind-induced plant motion immediately increases cytosolic calcium. Proc. Natl. Acad.
      Sci. USA 1992, 89, 4967–4971. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                     25 of 27




91.    Legué, V.; Blancaflor, E.; Wymer, C.; Perbal, G.; Fantin, D.; Gilroy, S. Cytoplasmic free Ca2+ in Arabidopsis roots changes in
       response to touch but not gravity. Plant Physiol. 1997, 114, 789–800. [CrossRef] [PubMed]
92.    Kurusu, T.; Kuchitsu, K.; Nakano, M.; Nakayama, Y.; Iida, H. Plant mechanosensing and Ca2+ transport. Trends Plant Sci. 2013,
       18, 227–233. [CrossRef] [PubMed]
93.    Monshausen, G.B.; Haswell, E.S. A force of nature: Molecular mechanisms of mechanoperception in plants. J. Exp. Bot. 2013, 64,
       4663–4680. [CrossRef] [PubMed]
94.    Fromm, J.; Lautner, S. Electrical signals and their physiological significance in plants. Plant Cell Environ. 2007, 30, 249–257.
       [CrossRef] [PubMed]
95.    Choi, W.G.; Hilleary, R.; Swanson, S.J.; Kim, S.H.; Gilroy, S. Rapid, long-distance electrical and calcium signaling in plants. Annu.
       Rev. Plant Biol. 2016, 67, 287–307. [CrossRef] [PubMed]
96.    Braam, J.; Davis, R.W. Rain-, wind-, and touch-induced expression of calmodulin and calmodulin-related genes in Arabidopsis.
       Cell 1990, 60, 357–364. [CrossRef]
97.    Nakagawa, Y.; Katagiri, T.; Shinozaki, K.; Qi, Z.; Tatsumi, H.; Furuichi, T.; Kishigami, A.; Sokabe, M.; Kojima, I.; Sato, S.; et al.
       Arabidopsis plasma membrane protein crucial for Ca2+ influx and touch sensing in roots. Proc. Natl. Acad. Sci. USA 2007,
       104, 3639–3644. [CrossRef]
98.    Nakano, M.; Iida, K.; Nyunoya, H.; Iida, H. Determination of structural regions important for Ca2+ uptake activity in Arabidopsis
       MCA1 and MCA2 expressed in yeast. Plant Cell Physiol. 2011, 52, 1915–1930. [CrossRef]
99.    Shigematsu, H.; Iida, K.; Nakano, M.; Chaudhuri, P.; Iida, H.; Nagayama, K. Structural characterization of the mechanosensitive
       channel candidate MCA2 from Arabidopsis thaliana. PLoS ONE 2014, 9, e87724. [CrossRef]
100.   Kamano, S.; Kume, S.; Iida, K.; Lei, K.J.; Nakano, M.; Nakayama, Y.; Iida, H. Transmembrane topologies of Ca2+ -permeable
       mechanosensitive channels MCA1 and MCA2 in Arabidopsis thaliana. J. Biol. Chem. 2015, 290, 30901–30909. [CrossRef] [PubMed]
101.   Nishii, K.; Möller, M.; Iida, H. Mix and match: Patchwork domain evolution of the land plant-specific Ca2+ -permeable
       mechanosensitive channel MCA. PLoS ONE 2021, 16, e0249735. [CrossRef]
102.   Furuichi, T.; Iida, H.; Sokabe, M.; Tatsumi, H. Expression of Arabidopsis MCA1 enhanced mechanosensitive channel activity in the
       Xenopus laevis oocyte plasma membrane. Plant Signal. Behav. 2012, 7, 1022–1026. [CrossRef] [PubMed]
103.   Yamanaka, T.; Nakagawa, Y.; Mori, K.; Nakano, M.; Imamura, T.; Kataoka, H.; Terashima, A.; Iida, K.; Kojima, I.; Katagiri, T.;
       et al. MCA1 and MCA2 that mediate Ca2+ uptake have distinct and overlapping roles in Arabidopsis. Plant Physiol. 2010,
       152, 1284–1296. [CrossRef]
104.   Hattori, T.; Otomi, Y.; Nakajima, Y.; Soga, K.; Wakabayashi, K.; Iida, H.; Hoson, T. MCA1 and MCA2 are involved in the response
       to hypergravity in Arabidopsis hypocotyls. Plants 2020, 9, 590. [CrossRef] [PubMed]
105.   Coste, B.; Mathur, J.; Schmidt, M.; Earley, T.J.; Ranade, S.; Petrus, M.J.; Dubin, A.E.; Patapoutian, A. Piezo1 and Piezo2 are
       essential components of distinct mechanically activated cation channels. Science 2010, 330, 55–60. [CrossRef] [PubMed]
106.   Guo, Y.R.; MacKinnon, R. Structure-based membrane dome mechanism for piezo mechanosensitivity. eLife 2017, 6, e33660.
       [CrossRef] [PubMed]
107.   Saotome, K.; Murthy, S.E.; Kefauver, J.M.; Whitwam, T.; Patapoutian, A.; Ward, A.B. Structure of the mechanically activated ion
       channel Piezo1. Nature 2018, 554, 481–486. [CrossRef] [PubMed]
108.   Zhao, Q.; Zhou, H.; Chi, S.; Wang, Y.; Wang, J.; Geng, J.; Wu, K.; Liu, W.; Zhang, T.; Dong, M.Q.; et al. Structure and mechanogating
       mechanism of the Piezo1 channel. Nature 2018, 554, 487–492. [CrossRef] [PubMed]
109.   Wang, Y.; Xiao, B. The mechanosensitive Piezo1 channel: Structural features and molecular bases underlying its ion permeation
       and mechanotransduction. J. Physiol. 2018, 596, 969–978. [CrossRef] [PubMed]
110.   Fang, X.Z.; Zhou, T.; Xu, J.Q.; Wang, Y.X.; Sun, M.M.; He, Y.J.; Pan, S.W.; Xiong, W.; Peng, Z.K.; Gao, X.H.; et al. Structure, kinetic
       properties and biological function of mechanosensitive Piezo channels. Cell Biosci. 2021, 11, 1–20. [CrossRef] [PubMed]
111.   Mousavi, S.A.R.; Dubin, A.E.; Zeng, W.Z.; Coombs, A.M.; Do, K.; Ghadiri, D.A.; Keenan, W.T.; Ge, C.; Zhao, Y.; Patapoutian,
       A. PIEZO ion channel is required for root mechanotransduction in Arabidopsis thaliana. Proc. Natl. Acad. Sci. USA 2021, 118,
       e2102188118. [CrossRef]
112.   Wu, J.; Lewis, A.H.; Grandl, J. Touch, tension, and transduction—The function and regulation of Piezo ion channels. Trends
       Biochem. Sci. 2017, 42, 57–71. [CrossRef]
113.   Zhang, Z.; Tong, X.; Liu, S.Y.; Chai, L.X.; Zhu, F.F.; Zhang, X.P.; Zou, J.Z.; Wang, X.B. Genetic analysis of a Piezo-like protein
       suppressing systemic movement of plant viruses in Arabidopsis thaliana. Sci. Rep. 2019, 9, 3187. [CrossRef]
114.   Fang, X.; Liu, B.; Shao, Q.; Huang, X.; Li, J.; Luan, S.; He, K. Atpiezo plays an important role in root cap mechanotransduction.
       Int. J. Mol. Sci. 2021, 22, 467. [CrossRef] [PubMed]
115.   Radin, I.; Richardson, R.A.; Coomey, J.H.; Weiner, E.R.; Bascom, C.S.; Li, T.; Bezanilla, M.; Haswell, E.S. Plant PIEZO homologs
       modulate vacuole morphology during tip growth. Science 2021, 373, 586–590. [CrossRef] [PubMed]
116.   Dünser, K.; Gupta, S.; Herger, A.; Feraru, M.I.; Ringli, C.; Kleine-Vehn, J. Extracellular matrix sensing by FERONIA and
       Leucine-Rich Repeat Extensins controls vacuolar expansion during cellular elongation in Arabidopsis thaliana. EMBO J. 2019,
       38, e100353. [CrossRef] [PubMed]
117.   Hou, C.; Tian, W.; Kleist, T.; He, K.; Garcia, V.; Bai, F.; Hao, Y.; Luan, S.; Li, L. DUF221 proteins are a family of osmosensitive
       calcium-permeable cation channels conserved across eukaryotes. Cell Res. 2014, 24, 632–635. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                                      26 of 27




118. Murthy, S.E.; Dubin, A.E.; Whitwam, T.; Jojoa-Cruz, S.; Cahalan, S.M.; Mousavi, S.A.R.; Ward, A.B.; Patapoutian, A.
     OSCA/TMEM63 are an evolutionarily conserved family of mechanically activated ion channels. eLife 2018, 7, e41844. [CrossRef]
     [PubMed]
119. Jojoa-Cruz, S.; Saotome, K.; Murthy, S.E.; Tsui, C.C.A.; Sansom, M.S.; Patapoutian, A.; Ward, A.B. Cryo-EM structure of the
     mechanically activated ion channel OSCA1.2. eLife 2018, 7, e41845. [CrossRef]
120. Liu, X.; Wang, J.; Sun, L. Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. Nat. Commun. 2018, 9, 1–9.
     [CrossRef]
121. Zhang, M.; Wang, D.; Kang, Y.; Wu, J.X.; Yao, F.; Pan, C.; Yan, Z.; Song, C.; Chen, L. Structure of the mechanosensitive OSCA
     channels. Nat. Struct. Mol. Biol. 2018, 25, 850–858. [CrossRef]
122. Maity, K.; Heumann, J.M.; McGrath, A.P.; Kopcho, N.J.; Hsu, P.K.; Lee, C.W.; Mapes, J.H.; Garza, D.; Krishnan, S.;
     Morgan, G.P.; et al. Cryo-EM structure of OSCA1.2 from Oryza sativa elucidates the mechanical basis of potential membrane
     hyperosmolality gating. Proc. Natl. Acad. Sci. USA 2019, 116, 14309–14318. [CrossRef]
123. Yuan, F.; Yang, H.; Xue, Y.; Kong, D.; Ye, R.; Li, C.; Zhang, J.; Theprungsirikul, L.; Shrift, T.; Krichilsky, B.; et al. OSCA1 mediates
     osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. Nature 2014, 514, 367–371. [CrossRef]
124. Thor, K.; Jiang, S.; Michard, E.; George, J.; Scherzer, S.; Huang, S.; Dindas, J.; Derbyshire, P.; Leitão, N.; DeFalco, T.A.;
     Köster, P.; et al. The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. Nature 2020, 585, 569–573.
     [CrossRef] [PubMed]
125. Cao, L.; Zhang, P.; Lu, X.; Wang, G.; Wang, Z.; Zhang, Q.; Zhang, X.; Wei, X.; Mei, F.; Wei, L.; et al. Systematic analysis of the
     maize OSCA genes revealing ZmOSCA family members involved in osmotic stress and ZmOSCA2.4 confers enhanced drought
     tolerance in transgenic arabidopsis. Int. J. Mol. Sci. 2020, 21, 351. [CrossRef] [PubMed]
126. Procko, C.; Murthy, S.; Keenan, W.T.; Mousavi, S.A.R.; Dabi, T.; Coombs, A.; Procko, E.; Baird, L.; Patapoutian, A.; Chory, J.
     Stretch-activated ion channels identified in the touch-sensitive structures of carnivorous droseraceae plants. eLife 2021, 10, e64250.
     [CrossRef] [PubMed]
127. Ryu, K.H.; Huang, L.; Kang, H.M.; Schiefelbein, J. Single-cell RNA sequencing resolves molecular relationships among individual
     plant cells. Plant Physiol. 2019, 179, 1444–1456. [CrossRef]
128. Shi, D.; Jouannet, V.; Agustí, J.; Kaul, V.; Levitsky, V.; Sanchez, P.; Mironova, V.V.; Greb, T. Tissue-specific transcriptome profiling
     of the Arabidopsis inflorescence stem reveals local cellular signatures. Plant Cell 2021, 33, 200–223. [CrossRef]
129. Sundell, D.; Street, N.R.; Kumar, M.; Mellerowicz, E.J.; Kucukoglu, M.; Johnsson, C.; Kumar, V.; Mannapperuma, C.;
     Delhomme, N.; Nilsson, O.; et al. Aspwood: High-spatial-resolution transcriptome profiles reveal uncharacterized modularity of
     wood formation in populus tremula. Plant Cell 2017, 29, 1585–1604. [CrossRef] [PubMed]
130. Jacobsen, A.G.; Jervis, G.; Xu, J.; Topping, J.F.; Lindsey, K. Root growth responses to mechanical impedance are regulated by a
     network of ROS, ethylene and auxin signalling in Arabidopsis. New Phytol. 2021, 231, 225–242. [CrossRef]
131. Lee, H.J.; Kim, H.S.; Park, J.M.; Cho, H.S.; Jeon, J.H. PIN-mediated polar auxin transport facilitates root-obstacle avoidance. New
     Phytol. 2020, 225, 1285–1296. [CrossRef]
132. Pomiès, L.; Decourteix, M.; Franchel, J.; Moulia, B.; Leblanc-Fournier, N. Poplar stem transcriptome is massively remodelled in
     response to single or repeated mechanical stimuli. BMC Genom. 2017, 18, 300. [CrossRef]
133. Colom, A.; Derivery, E.; Soleimanpour, S.; Tomba, C.; Molin, M.D.; Sakai, N.; González-Gaitán, M.; Matile, S.; Roux, A. A
     fluorescent membrane tension probe. Nat. Chem. 2018, 10, 1118–1125. [CrossRef]
134. Xing, L.; Zhang, D.; Qi, S.; Chen, X.; An, N.; Li, Y.; Zhao, C.; Han, M.; Zhao, J. Transcription profiles reveal the regulatory
     mechanisms of spur bud changes and flower induction in response to shoot bending in apple (Malus domestica Borkh.). Plant Mol.
     Biol. 2019, 99, 45–66. [CrossRef] [PubMed]
135. Alonso-Serra, J.; Safronov, O.; Lim, K.J.; Fraser-Miller, S.J.; Blokhina, O.B.; Campilho, A.; Chong, S.L.; Fagerstedt, K.; Haavikko, R.;
     Helariutta, Y.; et al. Tissue-specific study across the stem reveals the chemistry and transcriptome dynamics of birch bark. New
     Phytol. 2019, 222, 1816–1831. [CrossRef] [PubMed]
136. Lee, D.; Polisensky, D.H.; Braam, J. Genome-wide identification of touch- and darkness-regulated Arabidopsis genes: A focus on
     calmodulin-like and XTH genes. New Phytol. 2005, 165, 429–444. [CrossRef]
137. Autran, D.; Bassel, G.W.; Chae, E.; Ezer, D.; Ferjani, A.; Fleck, C.; Hamant, O.; Hartmann, F.P.; Jiao, Y.; Johnston, I.G.; et al. What is
     quantitative plant biology? Quant. Plant Biol. 2021, 2, e10. [CrossRef]
138. Iida, H. Mugifumi, a beneficial farm work of adding mechanical stress by treading to wheat and barley seedlings. Front. Plant Sci.
     2014, 5, 453. [CrossRef]
139. Morel, P.; Crespel, L.; Galopin, G.; Moulia, B. Effect of mechanical stimulation on the growth and branching of garden rose. Sci.
     Hortic. 2012, 135, 59–64. [CrossRef]
140. Gladala-Kostarz, A.; Doonan, J.H.; Bosch, M. Mechanical stimulation in Brachypodium distachyon: Implications for fitness,
     productivity, and cell wall properties. Plant Cell Environ. 2020, 43, 1314–1330. [CrossRef] [PubMed]
141. Ghosh, R.; Barbacci, A.; Leblanc-Fournier, N. Mechanostimulation: A promising alternative for sustainable agriculture practices.
     J. Exp. Bot. 2021, 72, 2877–2888. [CrossRef]
142. De Langre, E.; Penalver, O.; Hémon, P.; Frachisse, J.M.; Bogeat-Triboulot, M.B.; Niez, B.; Badel, É.; Moulia, B. Nondestructive and
     fast vibration phenotyping of plants. Plant Phenom. 2019, 2019, 6379693. [CrossRef]
Int. J. Mol. Sci. 2021, 22, 11043                                                                                             27 of 27




143. Hawcroft, M.; Walsh, E.; Hodges, K.; Zappa, G. Significantly increased extreme precipitation expected in Europe and North
     America from extratropical cyclones. Environ. Res. Lett. 2018, 13, 124006. [CrossRef]
144. Fournier, M.; Dlouhá, J.; Jaouen, G.; Alméras, T. Integrative biomechanics for tree ecology: beyond wood density and strength. J.
     Exp. Bot. 2013, 64, 4793–4815. [CrossRef] [PubMed]
145. Katoh, K.; Rozewicki, J.; Yamada, K.D. MAFFT online service: multiple sequence alignment, interactive sequence choice and
     visualization. Briefings Bioinform. 2017, 20, 1160–1166. [CrossRef]
146. Leek, J.T.; Johnson, W.E.; Parker, H.S.; Jaffe, A.E.; Storey, J.D. The sva package for removing batch effects and other unwanted
     variation in high-throughput experiments. Bioinformatics 2012, 28, 882–883. [CrossRef] [PubMed]
