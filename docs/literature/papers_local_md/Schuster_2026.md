# Schuster_2026

**Source PDF:** 

---

                                                                                                                                                                     Review



                                                              Tansley review
                                                              Desiccation tolerance mechanisms in the green
                                                              lineage and beyond

Author for correspondence:                                    Jenny Schuster1,2                  and Robert VanBuren1,2,3
Robert VanBuren                                               1
Email: vanbur31@msu.edu                                       Plant Resilience Institute, Michigan State University, East Lansing, MI 48824, USA; 2Department of Plant Biology, Michigan State
                                                              University, East Lansing, MI 48824, USA; 3Department of Plant, Soil, and Microbial Sciences, Michigan State University, East
Received: 10 March 2026                                       Lansing, MI 48824, USA
Accepted: 24 June 2026




Contents

       Summary                                                                         3159          IV. Biotechnological applications of desiccation tolerance to
                                                                                                         crops and beyond                                                               3169
I.     Introduction                                                                    3159
                                                                                                     V.    Concluding thoughts                                                          3170
II.    Core mechanisms underlying desiccation tolerance                                3161
                                                                                                           Acknowledgements                                                             3170
III.   The emergent complexity of desiccation tolerance
       in plants                                                                       3166                References                                                                   3171




                                                              Summary
New Phytologist (2026) 251: 3159–3175                         Water is essential for life on Earth, yet some plants can survive the near-complete loss of cellular
doi: 10.1111/nph.71466                                        water, a trait known as desiccation tolerance. Although rare in vegetative tissues of vascular
                                                              plants, desiccation tolerance is scattered across the plant kingdom, where it likely enabled early
Key words: convergent evolution, desiccation                  terrestrialization and supports survival in environments with prolonged or intermittent drying.
tolerance, plant resilience, systems biology,                 Large-scale multi-omics, comparative, and functional studies over the past decade suggest that
terrestrialization.                                           desiccation tolerance evolved primarily through the repurposing of ancient stress-resilience
                                                              mechanisms, giving rise to convergent phenotypes where cells are protected and stabilized
                                                              during extreme dehydration. In photosynthetic lineages, desiccation is further compounded by
                                                              light-dependent photooxidative stress, requiring specialized mechanisms that safeguard the
                                                              photosynthetic apparatus during both drying and recovery. Here, we synthesize our current
                                                              understanding of the evolutionary origins and core mechanisms underlying plant desiccation
                                                              tolerance and place them within a broader comparative context across kingdoms. We highlight
                                                              how genome-scale datasets suggest desiccation tolerance is an emergent, systems-level
                                                              phenotype coordinated across biological scales. Finally, we discuss the translational opportu-
                                                              nities and constraints of desiccation tolerance in agriculture, medicine, biotechnology, and
                                                              related fields.


                                                                                                     across many of Earth’s biomes, and organisms have evolved a
I. Introduction
                                                                                                     remarkable diversity of strategies to survive dehydration (Oliver
Life on Earth originated in water and nearly all biological                                          et al., 2020). One of the most striking biological innovations
macromolecules and cellular processes require a high internal                                        for surviving water limitation is desiccation tolerance, or the
water content to function (Womersley, 1981; Walters                                                  ability to survive the near-complete loss of cellular water
et al., 2005). Yet, water limitation is a pervasive challenge                                        (Bewley, 1979; Marks et al., 2025a). This trait has profoundly

Ó 2026 The Author(s).                                                                                                                  New Phytologist (2026) 251: 3159–3175 3159
New Phytologist Ó 2026 New Phytologist Foundation.                                                                                                           www.newphytologist.com
This is an open access article under the terms of the Creative Commons Attribution License, which permits use,
distribution and reproduction in any medium, provided the original work is properly cited.
                                                                                                                                                          14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                        New
3160 Review          Tansley review                                                                                                     Phytologist

     shaped the evolution of life on Earth. It enabled the recurrent          irradiance, and erratic rainfall. Unlike ecosystems shaped by
     colonization of land, particularly within the green lineage,             seasonal or prolonged drought, these habitats select for desicca-
     collectively known as Viridiplantae, and supported the                   tion tolerance rather than drought avoidance strategies. They
     long-term survival of seeds, pollen, spores, and other propagules        harbor diverse assemblages of desiccation-tolerant organisms,
     (Hoekstra et al., 2001). Desiccation tolerance also underpins            including terrestrial algae, bryophytes, ferns, angiosperms, fungi,
     the stability of dried microbial cultures used in food                   and microanimals that exhibit similar protective mechanisms
     production, biotechnology, and synthetic biology, and it                 despite vast evolutionary distances (Porembski & Barthlott, 2000;
     facilitates the storage and distribution of pharmaceuticals (Potts       Porembski et al., 2021; Vanschoenwinkel et al., 2025). Although
     et al., 2005; Marks et al., 2025a). Research on desiccation              rare, resurrection plants are scattered across the plant phylogeny
     tolerance has grown rapidly in recent decades (Lotreck                   (Oliver et al., 2000; Wood, 2007; VanBuren et al., 2019; Marks
     et al., 2024), yielding major advances in the genetic,                   et al., 2021a) and have become key models for studying both
     physiological, biochemical, and systems-level understanding of           extreme stress adaptations and the evolution of complex traits.
     mechanisms underlying this remarkable trait. From an evolu-                 Early land plants were likely poikilohydrous, with limited
     tionary perspective, desiccation tolerance has arisen repeatedly         ability to regulate internal water content independently of their
     across deep timescales and throughout the tree of life,                  surrounding environment. Fossil and phylogenetic evidence
     facilitating multiple independent transitions from aquatic to            suggests that these plants were small and lacked many of the
     terrestrial environments and enabling survival during periodic           vascular, rooting, and water-conserving features that evolved later
     drying across diverse habitats (Oliver et al., 2000; Alpert, 2005;       (Rubinstein et al., 2010; de Vries & Archibald, 2018; Morris
     Gaff & Oliver, 2013; Marks et al., 2021a). The ability to                et al., 2018; Fig. 1). However, as vascular tissues, stomata, and
     survive desiccation is widespread but sporadically distributed           other water-conserving innovations evolved, desiccation tolerance
     across archaea, bacteria, fungi, animal, and plant lineages              was lost from most vegetative tissues in favor of mechanisms that
     (Oliver et al., 2000; Alpert, 2006; Leprince & Buitink, 2015).           maintain internal water balance. These underlying desiccation
        Across nonplant lineages, desiccation tolerance is often restricted   tolerance mechanisms were retained in most spores, seeds, and
     to resistant propagules, resting cells, or dormant stages specialized    pollen, where they continue to support stress resistance,
     for persistence, whereas plant vegetative desiccation tolerance          dormancy, dispersal, and long-term survival through dry
     requires ordinary vegetative tissues to dry and then resume growth       conditions (Oliver et al., 2000; Alpert, 2005; Gaff &
     after rehydration. In animals, desiccation tolerance is found in         Oliver, 2013). More recently, these seed pathways were likely
     certain invertebrates, such as tardigrades, nematodes, rotifers, brine   co-opted and rewired in angiosperm resurrection plants to enable
     shrimp cysts (Artemia), and the sleeping chironomid (Polypedilum         vegetative desiccation tolerance, as supported by comparative
     vanderplanki; Crowe, 1971; Watanabe, 2006), all of which inhabit         genomic and transcriptomic studies (Cushman & Oliver, 2011;
     seasonal pools, soils, and surfaces that periodically dry. Many fungi    VanBuren et al., 2017; Costa et al., 2017b; Pardo et al., 2020).
     produce desiccation-tolerant propagules, including asexual con-          Consistent with this view, many of the gene families and
     idia, sexual ascospores, and basidiospores, and sclerotia, which         stress-response pathways underlying desiccation tolerance are
     enable survival in fluctuating or seasonally dry environments            conserved in streptophyte and chlorophyte algae, suggesting that
     (Kranner et al., 2008). In bacteria, extreme desiccation tolerance is    the molecular toolkit for surviving drying predates the terrestria-
     most well-studied in endospore-forming Firmicutes, such as               lization of plants (Rippin et al., 2017; Azar et al., 2025; Dadras
     Bacillus and Clostridium, whose multilayered spore coats and             et al., 2025). Together, these evolutionary patterns support the
     DNA-protective proteins allow persistence for decades or even            emerging view that desiccation tolerance is built from deeply
     centuries in a dormant state (Potts, 1994). Other bacterial taxa         conserved mechanisms, shaped by lineage-specific rewiring rather
     form cysts or other resistant cells that survive drying, including       than de novo innovation.
     many cyanobacteria inhabiting desert crusts (Potts, 1999).                  In this review, we examine the underlying mechanisms that have
     Although desiccation tolerance is less studied in archaea, some          enabled the evolution of desiccation tolerance across the green
     halophilic and thermophilic species can persist through desicca-         lineage and beyond. We explore how this trait has emerged
     tion, often within salt crusts or biofilms, and may form cyst-like       repeatedly through the recruitment of a shared molecular toolkit
     resting cells under stress (Potts, 1994).                                across vast evolutionary distances to stabilize cellular structures
        Within vascular plants, vegetative desiccation tolerance occurs       during extreme dehydration. We discuss hypotheses on the origin
     in a small group of species known as ‘resurrection plants’, named        of desiccation tolerance and how ancient protective pathways have
     for their seemingly miraculous recovery from near-complete and           been recurrently repurposed to enable life without water. We also
     typically lethal drying. Resurrection plants are often found in          highlight the unique challenges that desiccation poses for
     ecologically distinct but functionally convergent communities,           photosynthetic organisms, and how plants, algae, and cyanobac-
     such as rocky outcrops, marginal habitats in tropical and                teria mitigate the damaging effects of light and photooxidative
     subtropical regions, and even quick-drying surfaces of rocks or          stress in a dry state. Finally, we examine the emergent complexity of
     other plants in mesic environments (Gaff, 1977, 1987; Gaff &             desiccation tolerance revealed through cross-scale, systems-level
     Bole, 1986; Porembski, 2007, 2011; Porembski et al., 2021;               datasets, and discuss how this knowledge base may help us
     Smrithy et al., 2023). These environments experience rapid               understand and inform efforts to engineer stress tolerance in crops
     drying and rehydration cycles due to shallow soils, high                 and biotechnological systems.

     New Phytologist (2026) 251: 3159–3175                                                                                       Ó 2026 The Author(s).
     www.newphytologist.com                                                                          New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                                     14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                                       Tansley review          Review 3161




Fig. 1 Ancient origin and recurrent evolution of desiccation tolerance in the green lineage. An aquatic desiccation-sensitive ancestor gave rise to
chlorophytes and streptophytes. (1) During early streptophyte evolution, desiccation tolerance evolved in propagules, such as algal spores and plant spores
and was likely present in some vegetative tissues during terrestrialization. (2) As vascular plants diversified, vegetative desiccation tolerance was largely lost
in most lineages when improved water transport and water use strategies evolved, with desiccation tolerance becoming primarily restricted to reproductive
propagules, such as spores, seeds, and pollen. (3) In a small number of lineages, vegetative desiccation tolerance re-evolved through the co-option of
propagule desiccation tolerance mechanisms, giving rise to resurrection plants in both non angiosperm and angiosperm clades. Colors indicate desiccation
tolerance in vegetative tissues (blue) and propagules (red) and Xs denote loss of desiccation tolerance in sensitive lineages. DT, desiccation tolerant; DS,
desiccation sensitive.



II. Core mechanisms underlying desiccation tolerance                                1. Physical stabilization through vitrification and sugar
                                                                                    accumulation
Across the tree of life, organisms face the same fundamental cellular
stressors during extreme dehydration and desiccation. This                          Nonreducing sugars accumulate in nearly all desiccation-tolerant
includes mechanical and biochemical stress, protein instability,                    organisms during drying (Hoekstra et al., 2001; Reina-Bueno
aggregation and denaturation, loss of membrane fluidity, and                        et al., 2012; Tapia et al., 2015; Nguyen et al., 2022). Nonreducing
massive reduction in cell volume. Unwanted interactions occur as                    sugars are chemically stable and minimally reactive, which makes
cellular structure is dismantled, and proteins and macromolecules                   them less prone to degradation or unwanted reactions during
are brought into proximity with each other (Oliver et al., 2020).                   desiccation. Accumulation of nonreducing sugars, such as sucrose
Desiccation-tolerant organisms have evolved diverse mechanisms                      and trehalose, promotes the transition of the cytoplasm from a
to stabilize macromolecules, preserve cellular integrity, and                       gel-like state to a glassy, vitrified matrix (Fig. 2; Crowe et al., 1998a;
minimize damaging interactions. Many of these protective                            Buitink & Leprince, 2004). Vitrification, or the formation of a
functions are shared across desiccation-tolerant plants, inverte-                   biological glass, stabilizes the cellular environment by immobiliz-
brates, fungi, and bacteria, consistent with a combination of deeply                ing macromolecules and cellular components, relieving mechanical
conserved stress-response mechanisms, convergent evolution, and                     stress on membranes, and limiting undesirable molecular interac-
lineage-specific innovation. Rather than implying a single evolu-                   tions caused by cell shrinkage and cytoplasmic crowding.
tionary origin for desiccation tolerance across all lineages, these                 Nonreducing sugars have high glass transition temperatures, the
similarities suggest that desiccation tolerance has repeatedly drawn                temperature range at which a rigid, glassy structure becomes more
on ancient cellular stress-resilience pathways and modified them in                 viscous (Wolkers et al., 1998; Crowe et al., 1998a). This enables
different evolutionary contexts.                                                    biological glasses to preserve cellular structures for extended periods
   In addition to these core cellular challenges, photosynthetic                    in the dry state. Additionally, nonreducing sugars are hydrophilic
desiccation-tolerant organisms must mitigate photooxidative                         and can form hydrogen bonds with proteins and polar head groups
damage driven by high irradiance and ultraviolet radiation. Plants,                 of phospholipid membranes. As water is lost during drying,
green algae, and cyanobacteria address these stressors using                        nonreducing sugars can functionally replace water by forming
specialized photoprotective mechanisms that dissipate excess                        similar hydrogen bonds, preventing the denaturation of proteins
excitation energy and limit reactive oxygen species (ROS)                           and maintaining membrane fluidity during drying (Fig. 2; Clegg
formation. However, the extent, diversity, and functional                           et al., 1982; Crowe et al., 1998b).
importance of light-induced damage and photoprotection during                          Sucrose is the most prominent nonreducing sugar accumulated
desiccation remain understudied.                                                    during drying in most resurrection plants (Dace et al., 2023). In

Ó 2026 The Author(s).                                                                                                      New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                                   www.newphytologist.com
                                                                                                                                                                   14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                                 New
3162 Review          Tansley review                                                                                                              Phytologist




     Fig. 2 Shared cellular mechanisms underlying desiccation tolerance across the tree of life. Desiccation-tolerant organisms, including cyanobacteria, yeast,
     invertebrates, and resurrection plants use shared biochemical and biophysical mechanisms to survive extreme cellular dehydration. These mechanisms
     stabilize macromolecules, protect cellular structures, and mitigate oxidative stress during water loss. (a) Nonreducing sugars accumulate and vitrify the
     cytoplasm. (b) Nonreducing sugars and intrinsically disordered proteins (IDPs) form hydrogen bonds with membranes and proteins, replacing water and
     maintaining protein structure and membrane stability. (c) Chaperone proteins prevent protein denaturation and aggregation. (d) IDPs stabilize at low water
     contents and contribute to vitrification. (e) Antioxidants accumulate to manage overproduction of reactive oxygen species (ROS). (f) DNA damage can
     occur due to ROS accumulation or prolonged exposure to high light in the desiccated state.


     some species, sucrose can accumulate to 90% of dry weight in                    Tripogon lolliformis, its accumulation is lower than that of sucrose
     desiccated tissues (Bianchi et al., 1991; Whittaker et al., 2001;               (Adams et al., 1990; Moore et al., 2007; Williams et al., 2015).
     Zhang et al., 2016). This accumulation results from both de novo                Trehalose also varies across desiccation-tolerant animals, as some
     synthesis and starch degradation, based on increased activity of                tardigrades and rotifers accumulate very little trehalose, and some
     enzymes in the sucrose biosynthetic pathway and elevated break-                 tardigrade species appear to lack canonical trehalose biosynthetic
     down of starch (M€    uller et al., 1997; Whittaker et al., 2007). In           genes altogether (Boothby et al., 2017; Boothby & Pielak, 2017).
     Craterostigma and other Linderiaceae species, the unusual sugar                 However, low amounts of trehalose still contribute to desiccation
     octulose accumulates during drying and is later converted into                  tolerance in tardigrades by enhancing the function of cytoplasmic
     sucrose, contributing to the sugar pool for vitrification (Phillips             abundant heat soluble (CAHS) proteins that promote vitrification
     et al., 2008; Egert et al., 2015). Raffinose family oligosaccharides,           and cellular stabilization during drying (Nguyen et al., 2022).
     such as raffinose and stachyose, also accumulate in                             Despite differences in the identity and abundance of specific sugars,
     desiccation-tolerant seeds and leaves of resurrection plant species,            their shared role in promoting glass formation, stabilizing
     such as Xerophyta viscosa and Eragrostis nindensis, and contribute to           macromolecules, and replacing water highlights vitrification as a
     water replacement, vitrification, and protection from oxidative                 unifying mechanism of desiccation tolerance shaped by evolu-
     damage (Koster, 1991; Hincha et al., 2003; Nishizawa et al., 2008).             tionary constraints on maintaining cellular integrity in the absence
     Similarly, desiccation-tolerant cyanobacteria produce extracellular             of water.
     polysaccharide structures that function similarly to nonreducing
     sugars, stabilizing the cells during desiccation (Wright et al., 2005).
                                                                                     2. Specialized protective proteins
        Trehalose, another nonreducing disaccharide, has a
     well-characterized role in desiccation tolerance in yeast, nematodes,           In addition to sugars, desiccation-tolerant organisms rely heavily on
     and Artemia, and functions analogously to sucrose through                       proteins that perform protective functions during drying. Among
     stabilizing macromolecules in the dry state (Hibshman et al.,                   these, intrinsically disordered proteins (IDPs) play a particularly
     2020). Although trehalose is synthesized in some resurrection                   important role due to their structural flexibility and multi-
     plants, including Selaginella species, Myrothamnus flabellifolia, and           functionality. IDPs lack a fixed three-dimensional structure and

     New Phytologist (2026) 251: 3159–3175                                                                                                Ó 2026 The Author(s).
     www.newphytologist.com                                                                                   New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                      14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                         Tansley review        Review 3163


participate in diverse cellular processes (Wright & Dyson, 2015).            Protein-based protection is a central component of survival in
Desiccation tolerance IDPs (DT-IDPs) have hydrophilic proper-             the dry state. However, many of these DT-IDPs and other
ties that allow them to perform many protective functions similar to      protective proteins are also induced in desiccation-sensitive species
those of sugars, including facilitating vitrification and replacing       during drying, including in LEAs in recalcitrant seeds (Pammenter
bound water (Fig. 2). Like sugars, DT-IDPs are able to form               & Berjak, 1999) and vegetative tissues of sensitive relatives of
hydrogen bonds with membranes and other proteins during                   resurrection plants (VanBuren et al., 2018a; Pardo et al., 2020).
drying, substituting for water molecules to maintain membrane             Instead, desiccation tolerance appears to depend on the coordina-
fluidity and prevent protein denaturation (Sochava & Smir-                tion, timing, and magnitude of these responses.
nova, 1993; Boothby & Pielak, 2017). In addition, DT-IDPs are
also involved in scavenging ROS and function as chaperone
                                                                          3. Mitigating oxidative stress
proteins (Tunnacliffe & Wise, 2007; Liu et al., 2023).
   While DT-IDPs can form protective biological glasses, they also        In addition to structural and biochemical challenges imposed by
increase the glass transition temperature of sugar-based vitrified        water loss, desiccating cells experience severe oxidative stress
cytoplasm, thereby improving glass stability (Fig. 2; Elliott             throughout drying, in the dry state, and during rehydration,
et al., 1996; Kim et al., 2018). Late embryogenesis abundant              although the sources and consequences of ROS differ across these
(LEA) proteins, which contribute to vitrification in most                 phases. ROS can damage membranes, nucleic acids, and proteins
desiccation-tolerant organisms, increase the glass transition             and arise from electron leakage in mitochondrial and chloroplast
temperature of sucrose-based glasses in resurrection plants and           electron transport chains. During drying, declining water content
desiccation-tolerant seeds (Wolkers et al., 2001). Additionally, in       progressively restricts carbon fixation and photosynthetic electron
tardigrades, CAHS proteins act together with trehalose to                 transport, creating redox imbalance. In fully desiccated tissues,
strengthen biological glasses (Nguyen et al., 2022).                      photosynthesis is inactive, but retained pigments and photosyn-
   Heat shock proteins (HSPs) are present in all eukaryotic               thetic complexes can remain vulnerable to light-dependent
organisms and play a crucial role in the stabilization of                 oxidative damage. ROS production can also increase during
macromolecules during desiccation (Parsell & Lindquist, 1993;             recovery as respiration and photosynthesis resume. Thus, photo-
Richter et al., 2010; Hibshman et al., 2020). A family of HSPs            protection is a critical component of desiccation tolerance in
known as small heat shock proteins (sHSPs) have intrinsically             photosynthetic organisms and requires specialized structural,
disordered regions, similar to LEA and CAHS proteins, and act as          biochemical, and regulatory strategies not needed in most
molecular chaperones to prevent the denaturation and aggregation          nonphotosynthetic taxa.
of key proteins during desiccation and rehydration (Haslbeck &               Resurrection plants have evolved two major strategies for
Vierling, 2015; Hibshman et al., 2023; Mihailova et al., 2023).           reducing photooxidative stress during drying. Homoiochlorophyl-
sHSPs are expressed during the development of pollen and seeds            lous species retain and protect Chl and thylakoid membranes
and have been implicated in desiccation tolerance in vegetative           throughout desiccation, which allows faster recovery of photo-
plant tissues, as well as in other desiccation-tolerant organisms like    synthesis but increases the risk of light-dependent oxidative damage
tardigrades, nematodes, and Artemia (Alamillo et al., 1995;               while tissues are dry (Fig. 3; Tuba et al., 1998; Dinakar &
Wehmeyer & Vierling, 2000; Hibshman et al., 2020). While                  Bartels, 2012; Charuvi et al., 2015, 2019; Oliver et al., 2020). By
HSP70, a canonical HSP is upregulated in response to dehydration          contrast, poikilochlorophyllous species dismantle Chl and photo-
in plants and desiccation-tolerant invertebrates, its role appears to     synthetic structures during drying and rebuild them after
be a part of a general stress response rather than a mechanism            rehydration, reducing photooxidative risk in the dry state but
specific for desiccation tolerance (Aghaie & Tafreshi, 2020;              delaying photosynthetic recovery. Most resurrection plants are
Hibshman et al., 2020).                                                   homoiochlorophyllous, and this strategy is advantageous in
   Resurrection plants also rely on specialized proteins to protect       habitats with short, unpredictable wet periods (Tuba &
against oxidative and structural damage caused by exposure to             Lichtenthaler, 2011).
intense light. Early light-inducible proteins (ELIPs) in resurrection        Although homoiochlorophylly makes recovery from desiccation
plants and related high light-inducible proteins (HLIPs) in               much quicker, it also makes plants more susceptible to oxidative
desiccation-tolerant terrestrial cyanobacteria belong to the broader      stress. To counteract this, these species may employ both physical
light-harvesting-complex-like (LHC-like) protein superfamily, a           shielding mechanisms and biochemical reorganization of their
group of pigment-binding proteins that help protect photosyn-             photosystems (Tuba & Lichtenthaler, 2011; Zia et al., 2016). Some
thetic machinery from photooxidative damage (Fig. 3; Hutin                species physically protect themselves by folding or curling their
et al., 2003). Green algae and land plants also use members of the        leaves to shade them from direct sunlight (Schwab et al., 1989;
LHCSR and PsbS protein families to dissipate excess excitation            Bartak et al., 2006; Georgieva et al., 2009; Rafsanjani et al., 2015).
energy under high light (Peers et al., 2009; Tibiletti et al., 2016; Xu   Myrothamnus flabellifolius is unable to recover when leaf folding is
et al., 2022). In addition, Craterostigma plantagineum expresses a        restricted, suggesting this physical avoidance mechanism may be
plastid-localized DNA-binding protein (CpPTP) that translocates           required for recovery in some resurrection plants (Farrant
to the chloroplast. CpPTP has been proposed to downregulate               et al., 2003). In Craterostigma wilmsii, thylakoids migrate to one
chloroplast activity during drying (Phillips et al., 2002; Dinakar &      side of the chloroplast during dehydration, likely providing an
Bartels, 2012).                                                           additional layer of protection against direct light alongside leaf

Ó 2026 The Author(s).                                                                                         New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                      www.newphytologist.com
                                                                                                                                                                    14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                                  New
3164 Review          Tansley review                                                                                                               Phytologist




     Fig. 3 Photosynthetic adaptations to desiccation across organizational scales. Desiccation-tolerant plants employ structural, cellular, and molecular
     strategies to manage light energy and protect photosynthetic machinery during dehydration. (a) Hydrated. In hydrated tissues, chloroplasts are functional
     and the photosynthetic apparatus is operational. Light-harvesting complexes and photosystems drive electron transport, producing ATP and NADPH that
     fuel carbon fixation in the Calvin Cycle when CO2 is available. (b) Desiccated, homoiochlorophyllous species. Chl and photosynthetic structures are
     retained but protected during dehydration. During drying, stomatal closure and declining water content limit CO2 uptake and carbon fixation, creating
     redox imbalance while light absorption continues. As tissues enter the dry state, photosynthesis and electron transport are largely inactive, but retained
     pigments and photosynthetic complexes remain vulnerable to light-dependent oxidative damage. Stomata close and CO2 becomes limiting, halting the
     Calvin Cycle. LHCs detach from photosystems, ELIPs bind Chl and absorb excess energy, and the xanthophyll cycle dissipates excitation energy as heat
     during drying and early recovery. Plastoglobules accumulate in chloroplasts and damaged organelles may be recycled through autophagy during drying
     and rehydration, while protected chloroplasts remain intact for rapid recovery upon rehydration. (c) Desiccated, poikilochlorophyllous species.
     Photosynthetic structures are largely dismantled during drying. Thylakoid membranes, Chl, and photosystems are degraded, leaving lipid remnants within
     xeroplasts. The photosynthetic machinery is subsequently rebuilt during rehydration.


     folding (Cooper & Farrant, 2002; Costa et al., 2017b). Under                    energy captured by LHCII to be dissipated via carotenoids in a form
     desiccation, light-harvesting complexes (LHCII) detach from                     of nonphotochemical quenching (Fig. 3; Charuvi et al., 2015; Zia
     photosystem II (PSII) and PSIIs aggregate into semi-crystalline                 et al., 2016). Similarly, Chlamydomonas and other green algae
     arrays, which halts the light-dependent reactions, causing light                undergo state transitions under high light, where LHCII shifts from

     New Phytologist (2026) 251: 3159–3175                                                                                                 Ó 2026 The Author(s).
     www.newphytologist.com                                                                                    New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                    14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                       Tansley review        Review 3165


PSII to PSI to rebalance electron flow (Bellafiore et al., 2005).       rehydration (Dace et al., 1998). This strategy mirrors regulatory
Because desiccation also over-reduces the photosynthetic chain,         processes seen during seed maturation, where Chl breakdown and
similar transitions may provide photoprotection in desiccation-         mRNA storage prepare cells for desiccation and later reactivation.
tolerant algae and possibly chlorolichens (Gauslaa et al., 2012).       These parallels suggest that vegetative desiccation tolerance in
   Anthocyanins and carotenoids complement the physical                 poikilochlorophyllous plants may co-opt regulatory and catabolic
avoidance mechanisms of homoiochlorophyllous resurrection               programs originally evolved for seed desiccation (Cooper &
plants, and they accumulate to high levels on the outermost layers      Farrant, 2002; Costa et al., 2017b).
of leaves during drying (Fig. 3; Sherwin & Farrant, 1998; Farrant          Even when photoprotective mechanisms reduce light-induced
et al., 2003; Charuvi et al., 2019). These pigments absorb excess       damage, ROS can still accumulate during drying, dry storage, and
light and reduce Chl excitation, with anthocyanins also acting as       rehydration, making antioxidant defenses essential for desiccation
antioxidants. The accumulation of these pigments helps limit Chl        tolerance. Across the tree of life, desiccation-tolerant species rely on
overexcitation, reduce ROS accumulation, and protect leaves from        conserved antioxidant systems to mitigate ROS damage during
direct sunlight, which is especially important in homoiochlor-          dehydration and rehydration (Fig. 2), including nonenzymatic
ophyllous species that retain photosynthetic machinery during           antioxidants, such as glutathione, carotenoids, ascorbic acid, and
drying (Sherwin & Farrant, 1998). Cyanobacteria utilize specia-         tocopherols, and enzymes, such as superoxide dismutase (SOD),
lized protective molecules, like scytonemin and mycosporine-like        catalase, and glutathione reductase. These antioxidant systems are
amino acids, which act similarly to anthocyanins in plants by           found in diverse desiccation-tolerant species, including resurrec-
protecting against harmful UV radiation (Singh et al., 2010;            tion plants, seeds, tardigrades, nematodes, and midge larvae
Rastogi et al., 2015). Although these compounds are primarily           (Adhikari et al., 2009; Moore et al., 2009; Rizzo et al., 2010; Tyson
induced by UV exposure, they are important in extreme                   et al., 2012; Nesmelov et al., 2018; Giovannini et al., 2022). For
environments where high irradiance, UV exposure, and periodic           example, in the resurrection plant Haberlea rhodopensis, ascorbic
drying co-occur (Fleming & Castenholz, 2007). Similarly,                acid increases fivefold and glutathione increases 50-fold during
cyanobacterial photobionts in some lichens have been shown to           drying (Georgieva et al., 2017). Antioxidants such as 1- and 2-cys-
produce scytonemin and other photoprotectants (Nguyen                   peroxiredoxins, glyoxalase I family proteins, and zinc metallothio-
et al., 2013).                                                          nine are found in resurrection plants and desiccation-tolerant seeds
   While homoiochlorophyllous species invest heavily in retaining       but not in desiccation-sensitive species. Additionally, SOD and
and protecting their photosynthetic machinery, other desiccation-       glutathione reductase activity increase during drying in two
tolerant plants take the opposite approach. Poikilochlorophyllous       tardigrade species (Rizzo et al., 2010; Giovannini et al., 2022).
species dismantle their photosynthetic apparatus during drying and      While many antioxidants are not exclusive to desiccation-tolerant
rebuild it after rehydration, thereby minimizing the risk of light-     organisms, the high concentration and preservation of these
induced damage while desiccated (Fig. 3; Gaff, 1977; Vander             molecules in the dry state are hallmarks of desiccation tolerance
Willigen et al., 2001). This prevents ROS accumulation from Chl         (Kranner & Birtic, 2005). Even at low hydration levels in the glassy
overexcitation, but it results in a slower recovery, as the             state, some respiration and ROS production continue, but
photosynthetic machinery must be reassembled upon rehydration           antioxidant capacity persists, mitigating this damage (Far-
(Vander Willigen et al., 2001). In angiosperms, poikilochloro-          rant, 2000; Kranner et al., 2002).
phylly is observed only in monocots and is typically associated with
species adapted to hyper-arid environments or high-light savan-
                                                                        4. Cellular recycling and organelle repair
nahs, where retaining and protecting the photosynthetic machinery
during desiccation would be too costly (Proctor & Tuba, 2002).          Despite the protective mechanisms described above, some cellular
These divergent strategies reflect ecological trade-offs and distinct   damage during desiccation is unavoidable, especially across
photoprotective innovations that plants must evolve to survive          repeated dehydration and rehydration cycles. Desiccation-tolerant
desiccation in the presence of light.                                   organisms activate autophagy during drying and recovery to recycle
   Poikilochlorophylly depends on coordinated Chl catabolism,           damaged proteins, membranes, and organelles. Autophagy-related
transient photoprotection, and stored transcripts that allow the        processes are upregulated in resurrection plants, yeast, Artemia, and
photosynthetic apparatus to be dismantled during drying and             the sleeping chironomid, while programmed cell death pathways
rebuilt after rehydration. Chl degradation in resurrection plants       are reduced or suppressed (Ratnakumar et al., 2011; Lin
was initially thought to be nonenzymatic (Proctor & Tuba, 2002).        et al., 2016; Belott et al., 2024).
However, later work showed that poikilochlorophyllous plants               In photosynthetic organisms, autophagy may help recycle
degrade their Chl using the pheophorbide a oxygenase (PAO)/             photosynthetic machinery that is damaged during drying or from
phyllobin pathway, a process that mirrors Chl breakdown in              prolonged light exposure in the desiccated state Fig. 3. Unlike
senescent tissues (Christ et al., 2014). Anthocyanins accumulate        seeds, which dismantle chloroplasts during maturation and rebuild
during the early stages of rehydration, protecting the cell from ROS    them during germination, or senescing leaves, which dismantle
generation as the thylakoids and photosynthetic apparatus are           chloroplasts irreversibly, poikilochlorophyllous resurrection plants
reassembled (Sherwin & Farrant, 1998). To ensure a rapid                disassemble, and rapidly reassemble photosynthetic structures
recovery, poikilochlorophyllous species accumulate the transcripts      during desiccation and recovery over multiple drying/rehydration
necessary to reassemble the photosynthetic apparatus quickly upon       cycles (Ooms et al., 1993; Pogson & Albrecht, 2011). In the

Ó 2026 The Author(s).                                                                                       New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                    www.newphytologist.com
                                                                                                                                                         14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                       New
3166 Review          Tansley review                                                                                                    Phytologist

     homoiochlorophyllous eudicot Craterostigma pumilum, desicca-            specific to tardigrades, binds to DNA and protects it from radiation
     tion leads to an accumulation of plastoglobules, chloroplast            induced damage (Hashimoto et al., 2016). Dsup has been shown to
     fragmentation, and selective vacuolar degradation of damaged            reduce radiation damage in human cells and plants, and could
     thylakoid membranes, with some membrane fragments seques-               safeguard DNA from ROS associated damage during desiccation
     tered within plastoglobules. Thus, although homoiochlorophyl-           (Hashimoto et al., 2016; Kirke et al., 2020; Del Casino et al., 2024).
     lous species retain much of their photosynthetic machinery during       Given the repeated evolution of desiccation tolerance and shared
     drying, autophagy and vacuolar degradation may help remove              strategies across taxa, it is plausible that functionally similar DNA-
     damaged photosynthetic components during desiccation and                protective proteins exist in other desiccation-tolerant organisms,
     recovery (Charuvi et al., 2019; Fig. 3).                                although this is understudied. Together, these proteins comple-
        Xeroplasts, the desiccated chloroplasts of poikilochlorophyllous     ment enzymatic repair pathways and contribute to the broader
     species, resemble gerontoplasts, degraded, nonphotosynthetic            network of mechanisms that preserve genome integrity during
     chloroplasts in senescent tissues. Rather than being degraded, they     extreme dehydration.
     are reactivated and differentiate back into functional chloroplasts
     upon rehydration (Ingle et al., 2008). Plastoglobules have also been
                                                                             III. The emergent complexity of desiccation tolerance
     implicated in thylakoid membrane assembly during biogenesis and
                                                                             in plants
     disassembly during senescence (Rottet et al., 2015). Fractured
     thylakoid membranes might be repaired or recycled upon                  Desiccation tolerance is an emergent trait that arises from
     rehydration via co-option of these biogenesis or autophagy              numerous molecular, physiological, and cellular processes coordi-
     pathways in poikilochlorophyllous species (Besagni & Kess-              nated across time and space that give rise to a phenotype that cannot
     ler, 2013; Rottet et al., 2015; Charuvi et al., 2019).                  be predicted from single pathways in isolation. Understanding this
                                                                             complexity has only become possible through advances in genome-
                                                                             scale and systems-level approaches, together with a growing
     5. DNA damage and repair
                                                                             research community, which have brought the molecular mechan-
     DNA damage poses a major threat to genome integrity during              isms underlying desiccation tolerance into clearer focus (Gechev
     desiccation, largely due to oxidative stress and UV exposure during     et al., 2021; Tebele et al., 2021; Lotreck et al., 2024). As of mid-
     both drying and recovery. Although antioxidants and ROS-                2025, > 20 high-quality reference genomes and dozens of multi-
     scavenging enzymes protect cellular components, they cannot fully       omics studies have been published, profiling gene expression
     prevent DNA damage (Waterworth et al., 2019). Most desiccation-         (transcriptomics), metabolite profiles (metabolomics), protein
     associated DNA damage appears to arise indirectly through               accumulation and modification (proteomics), and chromatin and
     oxidative stress and dry-state exposure, making rapid repair            methylation dynamics (epigenomics) during desiccation and
     essential during recovery (Gladyshev & Meselson, 2008; Neumann          rehydration (Gechev et al., 2021; Gao et al., 2024). Collectively,
     et al., 2009; Gladyshev & Arkhipova, 2010; Gusev et al., 2010;          these large-scale datasets have revealed that desiccation tolerance is
     Rebecchi, 2013). The extreme radiation tolerance of many                an unexpectedly complex trait, involving far more regulatory and
     desiccation-tolerant organisms, including rotifers, Artemia, chir-      metabolic pathways than early single-gene studies suggested.
     onomid larvae, tardigrades, and seeds, is linked to efficient DNA       Tolerance is orchestrated through coordinated changes across time
     protection and repair systems (Gladyshev & Meselson, 2008;              and tissues at multiple biological levels. Comparative datasets
     Neumann et al., 2009; Gusev et al., 2010; Marcu et al., 2013;           across resurrection plants have demonstrated extensive network
     MacRae, 2016). These mechanisms include conserved pathways,             rewiring, most notably the co-option of seed developmental
     such as base excision repair, nucleotide excision repair, and double-   programs into vegetative tissues (VanBuren et al., 2017, 2018a;
     strand break repair, which are active during rehydration (Water-        Pardo et al., 2020). Shared molecular, physiological, biochemical,
     worth et al., 2019). For example, RAD51-mediated double-strand          and genomic signatures further support the existence of core
     break repair supports recovery from desiccation-related stress across   mechanisms underlying this trait. Yet despite these advances, many
     species, with rehydration-induced expression in Polypedilum             aspects of desiccation tolerance still remain poorly understood, and
     vanderplanki and reduced germination and survival in maize              its complexity continues to challenge our ability to model, predict,
     mutants (Li et al., 2007; Gusev et al., 2010). Oxidative lesions such   engineer, or fully reconstruct this phenotype.
     as 8-oxoguanine also accumulate in desiccating seeds and are                Before the 1980s, research on resurrection plants focused largely
     repaired by OGG1 and FPG during imbibition, while additional            on physiology and morphology, and the broader plant biology
     repair pathways such as nucleotide excision repair and DNA ligase       community was mostly unaware of these species (Bartels
     activity contribute to seed longevity and genome restoration during     et al., 2025). The molecular era began in 1990, when Dorothea
     germination (Macovei et al., 2011; Chen et al., 2012; Parreira          Bartels et al. (1990) first investigated desiccation tolerance at the
     et al., 2018).                                                          gene level in the resurrection plant Craterostigma plantagineum.
        In addition to repair, some proteins provide direct protection to    Using abscisic acid (ABA) pretreatment and differential cDNA
     DNA. Group II LEA proteins can bind DNA and may contribute              screening, they identified the first desiccation-inducible genes,
     to DNA protection, repair, or chromatin-associated processes            many encoding LEA proteins, linking vegetative desiccation
     during stress (Wise & Tunnacliffe, 2004; Banerjee & Roychoudh-          tolerance to seed dehydration pathways. This work catalyzed
     ury, 2016). Furthermore, the Damage Suppressor (Dsup) protein,          molecular studies of tolerance, revealing numerous protective

     New Phytologist (2026) 251: 3159–3175                                                                                      Ó 2026 The Author(s).
     www.newphytologist.com                                                                         New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                       14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                             Tansley review       Review 3167


genes, including dehydrins, ELIPs, antioxidants, and stress-               O. capense, and various Tripogon species, are diploid with small
responsive transcription factors. Early transcriptomic, proteomic,         c. 250-Mb genomes (VanBuren et al., 2015; Marks et al., 2024b).
and metabolomic studies later laid the groundwork for modern               Polyploidy is extremely common in grasses, and c. 90% of
systems-level analyses (Ingle et al., 2007; Jiang et al., 2007;            Chloridoid grasses are polyploid, regardless of tolerance (Roodt &
Rodriguez et al., 2010).                                                   Spies, 2003). While not essential for evolving tolerance,
                                                                           polyploidy may enhance it, as Microchloa afra genotypes with
                                                                           higher order ploidy are more desiccation-tolerant (Marks
1. Genome architecture and desiccation tolerance
                                                                           et al., 2024a). Similarly, genome size has been proposed as a
Genomic resources for resurrection plants initially lagged behind          factor for desiccation tolerance, as many resurrection plants have
those of model systems, crops, and economically relevant plants            relatively small monoploid genomes. Yet this pattern is incon-
(Marks et al., 2021b). This changed with the publication of the            sistent as several angiosperm resurrection plants and nearly all
high-quality genome for the resurrection grass Oropetium                   tolerant ferns have large, multi-gigabase genomes. Thus, genome
thomaeum, which provided new insights into the genetic basis of            architectures may facilitate or enhance desiccation tolerance in
desiccation tolerance (VanBuren et al., 2015, 2018b). Since then,          some lineages, but neither polyploidy nor genome size currently
genomes have been sequenced for numerous additional resurrec-              appears to be a universal predictor of the trait.
tion species (Table 1). These new genomic resources have enabled              Desiccation-tolerant animals like Polypedilum vanderplanki have
the community to test longstanding hypotheses about the genetic            evolved desiccation-associated gene islands, clusters of paralogous
basis of desiccation tolerance, including potential links to               genes encoding protective proteins that are highly expressed during
polyploidy (Marks et al., 2024a), the presence of desiccation-             drying (Gusev et al., 2014). Similar clusters of desiccation-
associated gene islands (Gusev et al., 2014; Costa et al., 2017a),         associated genes were identified in the resurrection plant Xerophyta
shifts in genome architecture, and the repurposing of ancestral            schlecteri (Costa et al., 2017a), but these patterns are difficult to
seed-related pathways (Gaff & Oliver, 2013).                               interpret as defining features of desiccation-tolerant plant genomes,
   One hypothesis proposes that polyploidy may have facilitated            as c. 20% of plant genes are tandemly duplicated, and some will
the evolution of desiccation tolerance, given its frequent                 inevitably be related to stress responses. Thus, neither polyploidy
association with increased environmental resilience in plants              nor changes in genome architecture are defining features of
(Lohaus & Van de Peer, 2016). Several resurrection grasses, such as        resurrection plants.
Eragrostis nindensis, Sporobolus stapfianus, and Microchloa afra, are         One notable exception to otherwise typical plant genome
complex polyploids. However, current evidence does not indicate            architecture in resurrection plants is the dramatic expansion of
that polyploidy is a defining feature of resurrection plants. Many         ELIP gene families. ELIPs are small photoprotective proteins that
related resurrection grasses, such as Oropetium thomaeum,                  help safeguard the photosynthetic machinery during light and


Table 1 Overview of sequenced resurrection plants.

                                                               Genome                                                    Desiccation tolerance
Species                       Clade          Family            size        References                      Ploidy        strategy

Selaginella lepidophylla      Lycophyte      Selaginellaceae     109 Mb    VanBuren et al. (2018c)         Diploid       Homoiochlorophyllous
Selaginella tamariscina       Lycophyte      Selaginellaceae     301 Mb    Xu et al. (2018)                Diploid       Homoiochlorophyllous
Selaginella sellowii          Lycophyte      Selaginellaceae    74.06 Mb   Alejo-Jacuinde et al. (2025)    Diploid       Homoiochlorophyllous
Syntrichia caninervis         Bryophyte      Pottiaceae         292.2 Mb   Silva et al. (2021)             Diploid       Homoiochlorophyllous
Syntrichia ruralis            Bryophyte      Pottiaceae        305.19 Mb   Zhang et al. (2024)             Diploid       Homoiochlorophyllous
Pohlia nutans                 Bryophyte      Mniaceae           698.2 Mb   Liu et al. (2022)               Diploid       Homoiochlorophyllous
Ceratodon purpureus           Bryophyte      Ditrichaceae        358 Mb    Carey et al. (2020)             Diploid       Homoiochlorophyllous
Fontinalis antipyretica       Bryophyte      Fontinalaceae      385.2 Mb   Yu et al. (2020)                Diploid       Homoiochlorophyllous
Boea hygrometrica             Angiosperm     Gesneriaceae       1691 Mb    Xiao et al. (2015)              Diploid       Homoiochlorophyllous
Craterostigma                 Angiosperm     Linderniaceae      1030 Mb    VanBuren et al. (2023)          Octoploid     Homoiochlorophyllous
 plantagineum
Lindernia brevidens           Angiosperm     Linderniaceae       270 Mb    VanBuren et al. (2018a)         Diploid       Homoiochlorophyllous
Myrothamnus flabellifolia     Angiosperm     Myrothamnaceae     1283 Mb    Marks et al. (2025b)            Diploid       Homoiochlorophyllous
Haberlea rhodopensis          Angiosperm     Gesneriaceae       1270 Mb    Gupta et al. (2024)             Diploid       Homoiochlorophyllous
Acanthochlamys bracteata      Angiosperm     Velloziaceae      197.97 Mb   Gao et al. (2021)               Diploid       Homoiochlorophyllous
Xerophyta schlechteri         Angiosperm     Velloziaceae       295.5 Mb   Costa et al. (2017a)            Octoploid     Poikilochlorophyllous
Sporobolus stapfianus         Angiosperm     Poaceae            1079 Mb    Montes et al. (2022)            Tetraploid    Homoiochlorophyllous
Microchloa afra               Angiosperm     Poaceae             968 Mb    Marks et al. (2024b)            Hexaploid     Homoiochlorophyllous
Oropetium capense             Angiosperm     Poaceae             237 Mb    Marks et al. (2024b)            Diploid       Homoiochlorophyllous
Tripogon minimus              Angiosperm     Poaceae             233 Mb    Marks et al. (2024b)            Diploid       Homoiochlorophyllous
Eragrostis nindensis          Angiosperm     Poaceae             986 Mb    Pardo et al. (2020)             Hexaploid     Poikilochlorophyllous
Oropetium thomaeum            Angiosperm     Poaceae             244 Mb    VanBuren et al. (2015, 2018b)   Diploid       Homoiochlorophyllous



Ó 2026 The Author(s).                                                                                          New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                       www.newphytologist.com
                                                                                                                                                         14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                       New
3168 Review          Tansley review                                                                                                    Phytologist

     dehydration stress (Hutin et al., 2003). Most land plants have one      desiccation-tolerant reproductive structures, such as seeds and
     to five ELIPs, but every sequenced resurrection plant genome            pollen, and comparative studies confirm that many protective genes
     harbors dozens to hundreds, often in large tandem arrays with           and processes are shared between desiccation-tolerant leaves and
     strong upregulation during desiccation and rehydration (VanBu-          desiccation-tolerant seeds. In resurrection grasses, desiccation-
     ren et al., 2019; Marks et al., 2024b). In angiosperms, these tandem    induced genes are enriched for ABI5 binding motifs, linking stress
     duplicates are highly similar in sequence, consistent with recent       responses in leaves to canonical seed maturation networks.
     lineage-specific expansions, whereas in nonseed plants, such as         Additionally, a novel drought-responsive cis-element upstream of
     bryophytes and lycophytes, ELIPs are more divergent and appear to       ELIPs in Oropetium thomaeum suggests regulatory neofunctiona-
     have arisen from more ancient duplications (VanBuren                    lization, enabling activation of photoprotective genes under
     et al., 2018c; Silva et al., 2021; Zhang et al., 2024; Alejo-           desiccation stress (St Aubin et al., 2022). In Xerophyta humilis
     Jacuinde et al., 2025). Within grasses, ELIP duplication occurred       and other resurrection plants, the canonical seed maturation
     independently in multiple Chloridoideae lineages, with Tripogo-         regulators (e.g. LEC1, ABI3, FUS3, and LEC2) are not upregulated
     ninae species showing tandem expansions on Chromosome 8 and             in vegetative tissues during drying, even though their downstream
     Eleusininae and Eragrostidinae on Chromosome 7 (Marks                   targets are strongly induced (Lyall et al., 2020). This points to a
     et al., 2024b). Massive ELIP expansions are also observed in            model where alternative regulators have been recruited to drive a
     desiccation-tolerant streptophytic algae, including within Zygne-       seed-like transcriptional program in leaves to rewire latent,
     matophyceae, the closest algal relatives of land plants (Feng           ancestral mechanisms that were never entirely lost.
     et al., 2024). Strikingly, duplication of ELIP homologs, the HLIPs,        Many seed-associated desiccation pathways are also activated in
     also occurs in desiccation-tolerant cyanobacteria. In the desert        desiccation-sensitive species under severe or lethal drought stress,
     cyanobacterium Nostoc flagelliforme, four tandemly repeated             but often as part of a broad, poorly coordinated stress response
     HLIPS confer protection during water deficit, and heterologous          (Pardo et al., 2020). In resurrection plants, these same or similar
     expression enhances desiccation tolerance in sensitive strains (Xu      pathways are deployed with greater coordination, timing, and
     et al., 2022). ELIP and HLIP tandem duplications are a striking         magnitude, allowing vegetative tissues to prepare for drying and
     example of convergent evolution, representing independent               recover after rehydration. Thus, the repeated emergence of
     expansions of the same gene family in response to similar selective     vegetative desiccation tolerance may depend less on novel
     pressures across cyanobacteria, algae, and land plants.                 protective mechanisms than on regulatory rewiring that reactivates
        Taken together, these findings indicate that features, such as       and coordinates existing stress-response pathways in the appro-
     polyploidy, genome size, and large-scale architectural changes, have    priate tissues and developmental context.
     had limited roles in the evolution of desiccation tolerance. Instead,      In desiccation-tolerant organisms, a component of this
     this trait likely evolved through the rewiring and redeployment of      coordination is the downregulation of metabolic processes, which
     existing genes and regulatory networks.                                 limits the accumulation of ROS and other toxic byproducts.
                                                                             Evidence from diverse lineages suggests that desiccation tolerance
                                                                             involves a coordinated transition to a low-metabolic or quiescent
     2. Recurrent evolution through regulatory reprogramming
                                                                             state. For example, desiccation-tolerant green algae are distin-
     In resurrection plants, time course transcriptomes show dramatic        guished from their desiccation-sensitive relatives by the down-
     shifts in gene expression, with thousands of coordinated changes        regulation of photosynthesis, starch metabolism, and generation of
     required to protect cellular macromolecules during drying and           metabolic intermediates (Peredo & Cardon, 2020). Similarly, the
     activate repair mechanisms upon rehydration (VanBuren                   shutdown of the circadian clock during desiccation in the
     et al., 2018a; Lin et al., 2019; Ostria-Gallardo et al., 2020; Pardo    resurrection grass Eragrostis nindensis may indicate that broader
     et al., 2020; Montes et al., 2022). Under moderate water loss,          regulatory networks are actively reprogrammed to facilitate entry
     expression patterns resemble typical drought responses, but as          into a quiescent state (Pardo, 2022). Vegetative desiccation
     tissues approach a critical water potential, a distinct desiccation-    tolerance may have re-evolved by re-coordinating latent programs
     specific program is activated. The cue for this transition remains      that enable a rapid and effective transition into this protected state
     unclear but may involve hydration-dependent biophysical signals,        under severe water deficit.
     such as the phase separation of seed-specific proteins like FLOE1 or       The extent to which this regulatory control is dynamic or
     SAM8 (Dorone et al., 2021; Wang et al., 2026).                          constitutive varies across lineages. Many desiccation-tolerant
        Many of the most abundant transcripts in desiccating                 bryophytes maintain high basal expression of protective genes
     angiosperm tissues encode classical seed dehydration proteins,          and antioxidants even when hydrated, minimizing the need for
     including LEAs, HSPs, ELIPs, oleosins, and enzymes involved in          transcriptional reprogramming during drying. Because these
     sugar metabolism (Cushman & Oliver, 2011; VanBuren                      poikilohydric species can desiccate rapidly in response to abrupt
     et al., 2017; Costa et al., 2017b; Pardo et al., 2020). This overlap    changes in humidity or water availability, they often persist in a
     suggests that vegetative desiccation tolerance in angiosperms likely    continuously primed state for desiccation and rehydration (Proctor
     evolved through the reactivation or expansion of pre-existing seed      et al., 2007; Alejo-Jacuinde et al., 2025). By contrast, angiosperms
     pathways, rather than through the de novo evolution of novel stress     typically experience more gradual declines in water availability,
     mechanisms (Oliver et al., 2000; Alpert, 2005; Gaff &                   allowing time for inducible gene expression programs that are
     Oliver, 2013; Marks et al., 2021a). Nearly all angiosperms produce      activated at low water potentials (Pardo et al., 2020). Differences

     New Phytologist (2026) 251: 3159–3175                                                                                      Ó 2026 The Author(s).
     www.newphytologist.com                                                                         New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                      14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                         Tansley review        Review 3169


among lineages reflect variation in how these programs are                 stress may provide similar avenues for improving tolerance.
deployed, on a spectrum from constitutive preparedness in                  Critically, many desiccation tolerance mechanisms are associated
poikilohydric species to tightly regulated, inducible responses in         with inherent fitness costs, including growth penalties, altered
angiosperms. In both cases, desiccation tolerance emerges from             carbon allocation, and reduced photosynthetic efficiency under
coordinated control of existing molecular machinery, reinforcing           nonstress conditions. These trade-offs likely reflect the energetic
the view that regulatory architecture, rather than gene content            and regulatory burden of maintaining a protective dry-state ready
alone, is the primary driver for the evolution of this complex trait.      physiology and help explain why desiccation tolerance has evolved
                                                                           in specialized ecological niches. Recognizing and managing these
                                                                           trade-offs will be essential for translating desiccation tolerance
IV. Biotechnological applications of desiccation
                                                                           mechanisms into crops, emphasizing strategies that deploy
tolerance to crops and beyond
                                                                           inducible or tissue-specific protection rather than constitutive
The extraordinary adaptations of desiccation-tolerant organisms            activation.
offer a rich reservoir of insights into how life persists under extreme       While modifying complex regulatory networks often risks
abiotic stress. These survival strategies illustrate the outer limits of   unintended downstream consequences, many desiccation tolerance
plant resilience but come with significant trade-offs. Resurrection        mechanisms are evolutionarily ancient, suggesting most plants may
plants often exhibit reduced metabolic rates, slower biomass               already harbor the genetic capacity for enhanced tolerance.
accumulation, and lower competitive ability, which limits the              Therefore, rather than introducing new genes, a more promising
feasibility of engineering crops that are fully desiccation-tolerant       strategy could involve strategic reconfiguration of these pre-existing
(Farrant & Hilhorst, 2022). Consequently, the challenge is not to          pathways, such as abscisic acid, autophagy, or senescence. This may
recreate desiccation tolerance in a sensitive crop, but to translate       reduce the downstream effects associated with the introduction of
this knowledge into practical applications. What can we learn from         foreign regulatory elements. For example, the ABA pathway is a
resurrection plants, and how can we use that information to                central hub for drought and desiccation responses in vegetative
enhance the resilience of crops without compromising yield or              tissues and seeds. The ABA receptor-ligand interaction is well
fitness? Rather than replicating desiccation tolerance, a more             characterized (Nishimura et al., 2009), and synthetic ligands that
promising approach is to introduce or enhance key protective               mimic ABA could be applied as foliar sprays or soil additives,
mechanisms, such as stress-responsive transcription factors,               enabling the activation of ABA pathways without genetic
osmoprotective sugars, antioxidants, and structural proteins into          engineering (Vaidya et al., 2019).
crop plants to improve their stress tolerance. Beyond agriculture,
these dry-state survival strategies may also inform applications in
                                                                           2. Applications of desiccation tolerance beyond agriculture
biotechnology and medicine, including improved preservation of
biological materials.                                                      While much attention has focused on the applications of
                                                                           desiccation tolerance research for crop resilience, resurrection
                                                                           plants offer significant potential in pharmacology and biotech-
1. Mechanistic approaches to crop improvement
                                                                           nology. Many species produce specialized metabolites with
Despite limitations on engineering a truly desiccation-tolerant            documented antioxidant, antiviral, and antibacterial activities
crop, many of the desiccation tolerance mechanisms discussed in            (Gescher et al., 2011; Kamng’ona et al., 2011; Gechev et al., 2014;
this review can be leveraged for improved stress tolerance in              Bentley et al., 2019a,b; Djilianov et al., 2024). Although these
sensitive organisms. Structural protectants show strong potential          properties are not necessarily unique to metabolites from
for crop improvement. Unlike regulatory elements, such as                  resurrection plants, the same protective systems that preserve
transcription factors, which can trigger wide-ranging and some-            cellular integrity during prolonged drying can also contribute to
times deleterious shifts in gene expression, structural proteins like      the stability of these metabolites in the dry state. As a result,
LEAs and sHSPs function primarily at the level of damage                   resurrection plants are a natural reservoir of biologically active
prevention and cellular stabilization and may cause fewer negative         compounds (Gescher et al., 2011; Kamng’ona et al., 2011;
downstream effects. Photosynthetic protection also offers promis-          Gechev et al., 2014; Bentley et al., 2019a,b; Djilianov
ing targets for improved tolerance in crops. Several pathways or           et al., 2024). For example, species like Myrothamnus flabellifolia
proteins have already been applied in model and crop systems.              and Haberlea rhodopensis produce polyphenols and glycosides
Overexpressing trehalose synthesis genes or DT-IDPs, such as               with documented antioxidant, antiviral, and antibacterial proper-
sHSPs and LEAs, has enhanced water stress tolerance in                     ties, offering resources for the cosmetic and pharmaceutical
Arabidopsis, tomato, rice, and tobacco (Garg et al., 2002; Cortina         industries (Gescher et al., 2011; Kamng’ona et al., 2011; Gechev
& Culian ~ez-Macia, 2005; Wang et al., 2006; Karim et al., 2007;         et al., 2014; Bentley et al., 2019a,b; Djilianov et al., 2024). Given
Xiao et al., 2007; Yu et al., 2016). Additionally, elevating the           the vast and largely unexplored diversity of plant secondary
expression of ELIPs increases abiotic stress tolerance (Zhuo               metabolites, resurrection plants may represent an untapped source
et al., 2013). Upregulating alternative sugar biosynthetic pathways        of novel bioactive compounds.
more commonly used in resurrection plants, such as sucrose or                 Furthermore, desiccation tolerance mechanisms hold promise
raffinose synthesis pathways, or minimizing photooxidative stress          for storage and transport of biological materials. Current gold-
by enhancing regulation of Chl degradation and reassembly during           standard storage methods for cells, tissues, vaccines, and medicines

Ó 2026 The Author(s).                                                                                         New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                      www.newphytologist.com
                                                                                                                                                             14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                           New
3170 Review          Tansley review                                                                                                        Phytologist

     require flash freezing and ultralow temperatures, which are costly         represent a shared core architecture across desiccation-tolerant
     and logistically demanding, making distribution inconvenient and           organisms or lineage-specific solutions to a common physiological
     limiting the range of distribution. However, by leveraging the             challenge.
     vitrification properties of trehalose and LEA proteins, which                 Expanding molecular and genomic toolkits offers promising
     stabilize cellular structures without requiring low temperatures,          avenues for exploring these open questions. Several resurrection
     researchers have successfully preserved mammalian cells, sperm,            plants have established transformation protocols (Furini
     and plant tissues in a dehydrated state (Guo et al., 2000; Chen            et al., 1994; Toth et al., 2006; Chowdhury et al., 2020), but
     et al., 2001; Gordon et al., 2001; McGinnis et al., 2005; Czernik          mechanistic studies remain limited and CRISPR approaches are
     et al., 2020; Zamecnik et al., 2021). Transitioning to dry-state           largely unexplored. Developing gene editing tools in these species
     storage could substantially improve the accessibility and distribu-        would enable direct functional testing of candidate regulators and
     tion of medical supplies by eliminating the need for ultralow-             gene functions underlying desiccation tolerance. Extending these
     temperature infrastructure.                                                approaches to desiccation-tolerant grasses could also facilitate
                                                                                translational applications in crop species. The increasing
                                                                                accessibility of single cell RNA sequencing further provides
     V. Concluding thoughts
                                                                                opportunities to resolve how distinct cell types coordinate
     The growing wealth of literature suggests that organisms across the        desiccation responses across tissues. Finally, broader comparative
     tree of life deploy similar molecular strategies to survive desiccation.   evolutionary and systems biology analyses that include closely
     However, research on desiccation tolerance has often been siloed           related species will help reconstruct the sequence in which key
     within specific study systems, with limited cross-disciplinary             traits evolved and deepen our understanding of how desiccation
     integration (Lotreck et al., 2024). As a result, conceptual advances       tolerance emerged.
     in one lineage are not always translated into broader mechanistic             The exceptional resilience of desiccation-tolerant organisms
     frameworks, constraining synthesis across biological scales and            offers a framework for understanding survival at environmental
     kingdoms. Here, we aimed to integrate discoveries from                     extremes and a rich source of molecular strategies that have diverse
     desiccation-tolerant plants with insights from other organisms,            practical applications. Improving plant resilience has been a
     highlighting common mechanisms that appear to be broadly                   longstanding challenge, as discoveries in the laboratory often fail to
     conserved across diverse lineages. These shared strategies have been       translate into improved performance in replicated field trials.
     repeatedly reactivated or repurposed during evolutionary transi-           Rather than engineering fully desiccation-tolerant crops, biotech-
     tions from aquatic to terrestrial environments, enabling survival in       nological efforts can focus on targeting downstream protectants
     extreme habitats and the dormancy and dispersal of propagules,             and endpoint metabolites. These molecules, shaped by evolution to
     such as seeds, spores, and pollen. As comparative datasets continue        function as cellular stabilizers, are attractive because they operate
     to expand, it is becoming clear that desiccation tolerance is not          largely outside of complex regulatory cascades. Beyond agriculture,
     governed by a single pathway but instead represents an emergent            the principles of desiccation tolerance are now being applied to
     phenotype arising from the coordinated interaction between                 stabilize biologics, enable dry-state storage of cells and vaccines, and
     numerous cellular, physiological, and regulatory systems.                  inspire synthetic biology innovations. In this way, resurrection
        Despite more than 6000 published studies on desiccation                 plants and other desiccation-tolerant lineages serve as both
     tolerance, critical knowledge gaps remain. A major unresolved              evolutionary case studies and engineering guides.
     question is when desiccation tolerance evolved and whether the
     underlying mechanisms reflect ancient conserved pathways that
                                                                                Acknowledgements
     were retained from early terrestrial ancestors or convergent
     solutions in which different genes and proteins provide similar            We thank reviewers as well as past and present members of the
     protective functions. Distinguishing between these possibilities will      VanBuren Lab for their helpful comments and suggestions. This
     require broader phylogenetic sampling and comparative analyses             work was funded by the Water and Life Interface Institute (NSF-
     that integrate genomic, biochemical, and physiological datasets            DBI-2213983) and NASA award 24-24SB_2-0171 to RV. JS was
     across kingdoms. In plants, we lack a complete understanding of            supported by the predoctoral training award T32-GM110523
     the upstream regulatory signals that distinguish drought responses         from the National Institute of General Medical Sciences of the
     from desiccation tolerance. These signals may involve transcrip-           NIH and the United States National Science Foundation Research
     tional or translational regulation, hormone signaling networks, or         Traineeship Program (NSF-NRT-1828149).
     poorly understood biophysical cues associated with declining
     cellular hydration. The spatial and temporal coordination of these
                                                                                Competing interests
     responses across tissues and cell types also remains largely
     unexplored. In addition, the extent of light-induced damage and            None declared.
     the role of photoprotective mechanisms in safeguarding macro-
     molecules remain poorly characterized. More broadly, it remains
                                                                                Author contributions
     unclear how the numerous protective pathways described here are
     integrated into regulatory networks that enable survival at                JS and RV conceived the review, prepared the figures, and wrote
     extremely low water contents, and whether these networks                   and edited the manuscript. Both authors approved the final version.

     New Phytologist (2026) 251: 3159–3175                                                                                          Ó 2026 The Author(s).
     www.newphytologist.com                                                                             New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                                                    14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                                                  Tansley review            Review 3171


ORCID                                                                                    Boothby TC, Tapia H, Brozena AH, Piszkiewicz S, Smith AE, Giovannini I,
                                                                                           Rebecchi L, Pielak GJ, Koshland D, Goldstein B. 2017. Tardigrades use
Jenny Schuster https://orcid.org/0009-0009-6919-6746                                       intrinsically disordered proteins to survive desiccation. Molecular Cell 65: 975–
Robert VanBuren https://orcid.org/0000-0003-2133-2760                                      984.
                                                                                         Buitink J, Leprince O. 2004. Glass formation in plant anhydrobiotes: survival in the
                                                                                           dry state. Cryobiology 48: 215–228.
References                                                                               Carey SB, Jenkins J, Lovell JT, Maumus F, Sreedasyam A, Payton AC, Shu S, Tiley
                                                                                           GP, Fernandez-Pozo N, Barry K et al. 2020. The Ceratodon purpureus genome
Adams RP, Kendall E, Kartha KK. 1990. Comparison of free sugars in growing and             uncovers structurally complex, gene rich sex chromosomes. bioRxiv. doi: 10.
  desiccated plants of Selaginella lepidophylla. Biochemical Systematics and Ecology       1101/2020.07.03.163634.
  18: 107–110.                                                                           Charuvi D, Nevo R, Aviv-Sharon E, Gal A, Kiss V, Shimoni E, Farrant JM,
Adhikari BN, Wall DH, Adams BJ. 2009. Desiccation survival in an Antarctic                 Kirchhoff H, Reich Z. 2019. Chloroplast breakdown during dehydration of a
  nematode: molecular analysis using expressed sequenced tags. BMC Genomics 10:            homoiochlorophyllous resurrection plant proceeds via senescence-like processes.
  69.                                                                                      Environmental and Experimental Botany 157: 100–111.
Aghaie P, Tafreshi SAH. 2020. Central role of 70-kDa heat shock protein in               Charuvi D, Nevo R, Shimoni E, Naveh L, Zia A, Adam Z, Farrant JM, Kirchhoff
  adaptation of plants to drought stress. Cell Stress & Chaperones 25: 1071–1081.          H, Reich Z. 2015. Photoprotection conferred by changes in photosynthetic
Alamillo J, Almoguera C, Bartels D, Jordano J. 1995. Constitutive expression of            protein levels and organization during dehydration of a homoiochlorophyllous
  small heat shock proteins in vegetative tissues of the resurrection plant                resurrection plant. Plant Physiology 167: 1554–1565.
  Craterostigma plantagineum. Plant Molecular Biology 29: 1093–1099.                     Chen H, Chu P, Zhou Y, Li Y, Liu J, Ding Y, Tsang EWT, Jiang L, Wu K, Huang
Alejo-Jacuinde G, Cha vez Montes RA, Gutierrez Reyes CD, Yong-Villalobos L,               S. 2012. Overexpression of AtOGG1, a DNA glycosylase/AP lyase, enhances seed
  Simpson J, Herrera-Estrella L. 2025. Gene family rearrangements and                      longevity and abiotic stress tolerance in Arabidopsis. Journal of Experimental
  transcriptional priming drive the evolution of vegetative desiccation tolerance in       Botany 63: 4107–4121.
  Selaginella. The Plant Journal 121: e17169.                                            Chen T, Acker JP, Eroglu A, Cheley S, Bayley H, Fowler A, Toner M. 2001.
Alpert P. 2005. The limits and frontiers of desiccation-tolerant life. Integrative and     Beneficial effect of intracellular trehalose on the membrane integrity of dried
  Comparative Biology 45: 685–695.                                                         mammalian cells. Cryobiology 43: 168–181.
Alpert P. 2006. Constraints of tolerance: why are desiccation-tolerant organisms so      Chowdhury SR, Hoque S, Akter N. 2020. Optimization of regeneration and
  small or rare? The Journal of Experimental Biology 209: 1575–1584.                       Agrobacterium tumefaciens-mediated transient transformation systems for
Azar M, Goldbecker E, Karpovsky D, Shpilman M, Breker M, de Vries J, Mosquna               Australian native extremophile, Tripogon loliiformis. Journal of King Saud
  A. 2025. Shared abscisic acid biosynthesis pathway across 600 million years of           University, Science 32: 3476–3485.
  streptophyte evolution. Plant Physiology 198: kiaf121.                                 Christ B, Egert A, S€ussenbacher I, Kr€a utler B, Bartels D, Peters S, H€ortensteiner S.
Banerjee A, Roychoudhury A. 2016. Group II late embryogenesis abundant (LEA)               2014. Water deficit induces chlorophyll degradation via the ‘PAO/phyllobilin’
  proteins: structural and functional aspects in plant abiotic stress. Plant Growth        pathway in leaves of homoio- (Craterostigma pumilum) and poikilochlorophyllous
  Regulation 79: 1–17.                                                                     (Xerophyta viscosa) resurrection plants: chlorophyll breakdown in resurrection
Barta k M, Solhaug KA, Vrablıkova H, Gauslaa Y. 2006. Curling during desiccation       plants. Plant, Cell & Environment 37: 2521–2531.
  protects the foliose lichen Lobaria pulmonaria against photoinhibition. Oecologia      Clegg JS, Seitz P, Seitz W, Hazlewood CF. 1982. Cellular responses to extreme
  149: 553–560.                                                                            water loss: the water-replacement hypothesis. Cryobiology 19: 306–316.
Bartels D, Giarola V, Chandler J. 2025. Unravelling the molecular network of             Cooper K, Farrant JM. 2002. Recovery of the resurrection plant Craterostigma
  desiccation tolerance in resurrection plants started with the model plant                wilmsii from desiccation: protection versus repair. Journal of Experimental Botany
  Craterostigma plantagineum. Planta 262: 37.                                              53: 1805–1813.
Bartels D, Schneider K, Terstappen G, Piatkowski D, Salamini F. 1990. Molecular                            ~ez-Macia FA. 2005. Tomato abiotic stress enhanced tolerance by
                                                                                         Cortina C, Culia n
  cloning of abscisic acid-modulated genes which are induced during desiccation of         trehalose biosynthesis. Plant Science 169: 75–82.
  the resurrection plant Craterostigma plantagineum. Planta 181: 27–34.                  Costa M-CD, Artur MAS, Maia J, Jonkheer E, Derks MFL, Nijveen H, Williams
Bellafiore S, Barneche F, Peltier G, Rochaix J-D. 2005. State transitions and light        B, Mundree SG, Jimenez-Gomez JM, Hesselink T et al. 2017a. A footprint of
  adaptation require chloroplast thylakoid protein kinase STN7. Nature 433: 892–           desiccation tolerance in the genome of Xerophyta viscosa. Nature Plants 3: 17038.
  895.                                                                                   Costa M-CD, Cooper K, Hilhorst HWM, Farrant JM. 2017b. Orthodox seeds and
Belott CJ, Gusev OA, Kikawada T, Menze MA. 2024. Membraneless and                          resurrection plants: two of a kind? Plant Physiology 175: 589–599.
  membrane-bound organelles in an anhydrobiotic cell line are protected from             Crowe JH. 1971. Anhydrobiosis: an unsolved problem. The American Naturalist
  desiccation-induced damage. Cell Stress & Chaperones 29: 425–436.                        105: 563–573.
Bentley J, Moore JP, Farrant JM. 2019a. Metabolomics as a complement to                  Crowe JH, Carpenter JF, Crowe LM. 1998a. The role of vitrification in
  phylogenetics for assessing intraspecific boundaries in the desiccation-tolerant         anhydrobiosis. Annual Review of Physiology 60: 73–103.
  medicinal shrub Myrothamnus flabellifolia (Myrothamnaceae). Phytochemistry             Crowe JH, Clegg JS, Crowe LM. 1998b. Anhydrobiosis: the water replacement
  159: 127–136.                                                                            hypothesis. In: The properties of water in foods ISOPOW 6. Boston, MA, USA:
Bentley J, Moore JP, Farrant JM. 2019b. Metabolomic profiling of the desiccation-          Springer US, 440–455.
  tolerant medicinal shrub Myrothamnus flabellifolia indicates phenolic variability      Cushman JC, Oliver MJ. 2011. Understanding vegetative desiccation tolerance
  across its natural habitat: implications for tea and cosmetics production. Molecules     using integrated functional genomics approaches within a comparative
  24: 1240.                                                                                evolutionary framework. In: Ecological studies: analysis and synthesis. Berlin,
Besagni C, Kessler F. 2013. A mechanism implicating plastoglobules in                      Heidelberg, New York NY. Plant desiccation tolerance. Berlin, Heidelberg,
  thylakoid disassembly during senescence and nitrogen starvation. Planta 237:             Germany: Springer Berlin Heidelberg, 307–338.
  463–470.                                                                               Czernik M, Fidanza A, Luongo FP, Valbonetti L, Scapolo PA, Patrizio P, Loi P.
Bewley JD. 1979. Physiological aspects of desiccation tolerance. Annual Review of          2020. Late embryogenesis abundant (LEA) proteins confer water stress tolerance
  Plant Physiology 30: 195–238.                                                            to mammalian somatic cells. Cryobiology 92: 189–196.
Bianchi G, Gamba A, Murelli C, Salamini F, Bartels D. 1991. Novel carbohydrate           Dace H, Sherwin HW, Illing N, Farrant JM. 1998. Use of metabolic inhibitors to
  metabolism in the resurrection plant Craterostigma plantagineum. The Plant               elucidate mechanisms of recovery from desiccation stress in the resurrection plant
  Journal 1: 355–359.                                                                      Xerophyta humilis. Plant Growth Regulation 24: 171–177.
Boothby TC, Pielak GJ. 2017. Intrinsically disordered proteins and desiccation           Dace HJ, Adetunji AE, Moore JP, Farrant JM, Hilhorst HW. 2023. A review of the
  tolerance: elucidating functional and mechanistic underpinnings of                       role of metabolites in vegetative desiccation tolerance of angiosperms. Current
  anhydrobiosis. BioEssays 39: 1700119.                                                    Opinion in Plant Biology 75: 102410.


Ó 2026 The Author(s).                                                                                                                New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                                             www.newphytologist.com
                                                                                                                                                                                         14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                                                     New
3172 Review            Tansley review                                                                                                                                Phytologist

     Dadras A, Duminil P, de Vries S, Irisarri I, Feussner I, de Vries J. 2025. Algal         Georgieva K, R€oding A, B€     uchel C. 2009. Changes in some thylakoid membrane
       origins of core land plant stress response subnetworks. The Plant Journal 122:            proteins and pigments upon desiccation of the resurrection plant Haberlea
       e70291.                                                                                   rhodopensis. Journal of Plant Physiology 166: 1520–1528.
     Del Casino C, Conti V, Licata S, Cai G, Cantore A, Ricci C, Cantara S. 2024.             Gescher K, K€   uhn J, Lorentzen E, Hafezi W, Derksen A, Deters A, Hensel A. 2011.
       Mitigation of UV-B radiation stress in tobacco pollen by expression of the                Proanthocyanidin-enriched extract from Myrothamnus flabellifolia Welw. exerts
       tardigrade damage suppressor protein (Dsup). Cells 13: 840.                               antiviral activity against herpes simplex virus type 1 by inhibition of viral
     Dinakar C, Bartels D. 2012. Light response, oxidative stress management and                 adsorption and penetration. Journal of Ethnopharmacology 134: 468–474.
       nucleic acid stability in closely related Linderniaceae species differing in           Giovannini I, Corsetto PA, Altiero T, Montorfano G, Guidetti R, Rizzo AM,
       desiccation tolerance. Planta 236: 541–555.                                               Rebecchi L. 2022. Antioxidant response during the kinetics of anhydrobiosis in
     Djilianov D, Moyankova D, Mladenov P, Topouzova-Hristova T, Kostadinova A,                  two eutardigrade species. Life 12: 817.
       Staneva G, Zasheva D, Berkov S, Simova-Stoilova L. 2024. Resurrection plants-          Gladyshev E, Meselson M. 2008. Extreme resistance of bdelloid rotifers to ionizing
       A valuable source of natural bioactive compounds: from word-of-mouth to                   radiation. Proceedings of the National Academy of Sciences, USA 105: 5139–5144.
       scientifically proven sustainable use. Metabolites 14: 113.                            Gladyshev EA, Arkhipova IR. 2010. Genome structure of bdelloid rotifers: shaped
     Dorone Y, Boeynaems S, Flores E, Jin B, Hateley S, Bossi F, Lazarus E, Pennington           by asexuality or desiccation? The Journal of Heredity 101: S85–S93.
       JG, Michiels E, De Decker M et al. 2021. A prion-like protein regulator of seed        Gordon SL, Oppenheimer SR, Mackay AM, Brunnabend J, Puhlev I, Levine F.
       germination undergoes hydration-dependent phase separation. Cell 184: 4284–               2001. Recovery of human mesenchymal stem cells following dehydration and
       4298.                                                                                     rehydration. Cryobiology 43: 182–187.
     Egert A, Eicher B, Keller F, Peters S. 2015. Evidence for water deficit-induced mass     Guo N, Puhlev I, Brown DR, Mansbridge J, Levine F. 2000. Trehalose expression
       increases of raffinose family oligosaccharides (RFOs) in the leaves of three              confers desiccation tolerance on human cells. Nature Biotechnology 18: 168–171.
       Craterostigma resurrection plant species. Frontiers in Physiology 6: 206.              Gupta S, Petrov V, Garg V, Mueller-Roeber B, Fernie AR, Nikoloski Z, Gechev T.
     Elliott B, Haltiwanger RS, Futcher B. 1996. Synergy between trehalose and                   2024. The genome of Haberlea rhodopensis provides insights into the mechanisms
       Hsp104 for thermotolerance in Saccharomyces cerevisiae. Genetics 144: 923–933.            for tolerance to multiple extreme environments. Cellular and Molecular Life
     Farrant JM. 2000. A comparison of mechanisms of desiccation tolerance among                 Sciences 81: 117.
       three angiosperm resurrection plant species. Plant Ecology 151: 29–39.                 Gusev O, Nakahara Y, Vanyagina V, Malutina L, Cornette R, Sakashita T,
     Farrant JM, Hilhorst H. 2022. Crops for dry environments. Current Opinion in                Hamada N, Kikawada T, Kobayashi Y, Okuda T. 2010. Anhydrobiosis-
       Biotechnology 74: 84–91.                                                                  associated nuclear DNA damage and repair in the sleeping chironomid: linkage
     Farrant JM, Vander Willigen C, Loffell DA, Bartsch S, Whittaker A. 2003. An                 with radioresistance. PLoS ONE 5: e14008.
       investigation into the role of light during desiccation of three angiosperm            Gusev O, Suetsugu Y, Cornette R, Kawashima T, Logacheva MD, Kondrashov AS,
       resurrection plants. Plant, Cell & Environment 26: 1275–1286.                             Penin AA, Hatanaka R, Kikuta S, Shimura S et al. 2014. Comparative genome
     Feng X, Zheng J, Irisarri I, Yu H, Zheng B, Ali Z, de Vries S, Keller J, F€urst-Jansen      sequencing reveals genomic signature of extreme desiccation tolerance in the
       JMR, Dadras A et al. 2024. Genomes of multicellular algal sisters to land plants          anhydrobiotic midge. Nature Communications 5: 4784.
       illuminate signaling network evolution. Nature Genetics 56: 1018–1031.                 Hashimoto T, Horikawa DD, Saito Y, Kuwahara H, Kozuka-Hata H, Shin-I T,
     Fleming ED, Castenholz RW. 2007. Effects of periodic desiccation on the synthesis           Minakuchi Y, Ohishi K, Motoyama A, Aizu T et al. 2016. Extremotolerant
       of the UV-screening compound, scytonemin, in cyanobacteria. Environmental                 tardigrade genome and improved radiotolerance of human cultured cells by
       Microbiology 9: 1448–1455.                                                                tardigrade-unique protein. Nature Communications 7: 12808.
     Furini A, Koncz C, Salamini F, Bartels D. 1994. Agrobacterium-mediated                   Haslbeck M, Vierling E. 2015. A first line of stress defense: small heat shock proteins
       transformation of the desiccation-tolerant plant Craterostigma plantagineum.              and their function in protein homeostasis. Journal of Molecular Biology 427: 1537–
       Plant Cell Reports 14: 102–106.                                                           1548.
     Gaff DF. 1977. Desiccation tolerant vascular plants of southern Africa. Oecologia 31:    Hibshman JD, Carra S, Goldstein B. 2023. Tardigrade small heat shock proteins
       95–109.                                                                                   can limit desiccation-induced protein aggregation. Communications Biology 6:
     Gaff DF. 1987. Desiccation tolerant plants in South America. Oecologia 74: 133–             121.
       136.                                                                                   Hibshman JD, Clegg JS, Goldstein B. 2020. Mechanisms of desiccation tolerance:
     Gaff DF, Bole PV. 1986. Resurrection grasses in India. Oecologia 71: 159–160.               themes and variations in brine shrimp, roundworms, and tardigrades. Frontiers in
     Gaff DF, Oliver M. 2013. The evolution of desiccation tolerance in angiosperm               Physiology 11: 592016.
       plants: a rare yet common phenomenon. Functional Plant Biology 40: 315–328.            Hincha DK, Zuther E, Heyer AG. 2003. The preservation of liposomes by raffinose
     Gao B, Li X, Liang Y, Chen M, Liu H, Liu Y, Wang J, Zhang J, Zhang Y, Oliver MJ             family oligosaccharides during drying is mediated by effects on fusion and lipid
       et al. 2024. Drying without dying: a genome database for desiccation-tolerant             phase transitions. Biochimica et Biophysica Acta 1612: 172–177.
       plants and evolution of desiccation tolerance. Plant Physiology 194: 2249–2262.        Hoekstra FA, Golovina EA, Buitink J. 2001. Mechanisms of plant desiccation
     Gao Z-Y, Li Z-H, Lin D-L, Jin X-H. 2021. Chromosome-scale genome assembly of                tolerance. Trends in Plant Science 6: 431–438.
       the resurrection plant Acanthochlamys bracteata (Velloziaceae). Genome Biology         Hutin C, Nussaume L, Moise N, Moya I, Kloppstech K, Havaux M. 2003. Early
       and Evolution 13: evab147.                                                                light-induced proteins protect Arabidopsis from photooxidative stress.
     Garg AK, Kim J-K, Owens TG, Ranwala AP, Choi YD, Kochian LV, Wu RJ. 2002.                   Proceedings of the National Academy of Sciences, USA 100: 4921–4926.
       Trehalose accumulation in rice plants confers high tolerance levels to different       Ingle RA, Collett H, Cooper K, Takahashi Y, Farrant JM, Illing N. 2008.
       abiotic stresses. Proceedings of the National Academy of Sciences, USA 99: 15898–         Chloroplast biogenesis during rehydration of the resurrection plant Xerophyta
       15903.                                                                                    humilis: parallels to the etioplast-chloroplast transition. Plant, Cell & Environment
     Gauslaa Y, Coxson DS, Solhaug KA. 2012. The paradox of higher light tolerance               31: 1813–1824.
       during desiccation in rare old forest cyanolichens than in more widespread co-         Ingle RA, Schmidt UG, Farrant JM, Thomson JA, Mundree SG. 2007. Proteomic
       occurring chloro- and cephalolichens. New Phytologist 195: 812–822.                       analysis of leaf proteins during dehydration of the resurrection plant Xerophyta
     Gechev T, Lyall R, Petrov V, Bartels D. 2021. Systems biology of resurrection               viscosa. Plant, Cell & Environment 30: 435–446.
       plants. Cellular and Molecular Life Sciences 78: 6365–6394.                            Jiang G, Wang Z, Shang H, Yang W, Hu Z, Phillips J, Deng X. 2007. Proteome
     Gechev TS, Hille J, Woerdenbag HJ, Benina M, Mehterov N, Toneva V, Fernie                   analysis of leaves from the resurrection plant Boea hygrometrica in response to
       AR, Mueller-Roeber B. 2014. Natural products from resurrection plants:                    dehydration and rehydration. Planta 225: 1405–1420.
       potential for medical applications. Biotechnology Advances 32: 1091–1101.              Kamng’ona A, Moore JP, Lindsey G, Brandt W. 2011. Inhibition of HIV-1 and M-
     Georgieva K, Dagnon S, Gesheva E, Bojilov D, Mihailova G, Doncheva S. 2017.                 MLV reverse transcriptases by a major polyphenol (3,4,5 tri-O-galloylquinic acid)
       Antioxidant defense during desiccation of the resurrection plant Haberlea                 present in the leaves of the South African resurrection plant, Myrothamnus
       rhodopensis. Plant Physiology and Biochemistry 114: 51–59.                                flabellifolia. Journal of Enzyme Inhibition and Medicinal Chemistry 26: 843–853.



     New Phytologist (2026) 251: 3159–3175                                                                                                             Ó 2026 The Author(s).
     www.newphytologist.com                                                                                                New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                                                  14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                                                 Tansley review           Review 3173


Karim S, Aronsson H, Ericson H, Pirhonen M, Leyman B, Welin B, M€antyl€a E,               Marks RA, Hotaling S, Frandsen PB, VanBuren R. 2021b. Representation and
   Palva ET, Van Dijck P, Holmstr€om K-O. 2007. Improved drought tolerance                  participation across 20 years of plant genome sequencing. Nature Plants 7: 1571–
   without undesired side effects in transgenic plants producing trehalose. Plant           1578.
   Molecular Biology 64: 371–386.                                                         Marks RA, Lovell JT, Carey SB, Van Der Pas L, Chimukuche NM, Br        una T, Plott
Kim SX, C  ß amdere G, Hu X, Koshland D, Tapia H. 2018. Synergy between the                 C, Webber J, Lipzen A, Yan J et al. 2025b. The architecture of resilience: a
   small intrinsically disordered protein Hsp12 and trehalose sustain viability after       genome assembly of Myrothamnus flabellifoliasheds Light on desiccation tolerance
   severe desiccation. eLife 7: e38337.                                                     and sex determination. New Phytologist 249: 1063–1084.
Kirke J, Jin X-L, Zhang X-H. 2020. Expression of a tardigrade Dsup gene enhances          Marks RA, Van Der Pas L, Schuster J, Gilman IS, VanBuren R. 2024b. Convergent
   genome protection in plants. Molecular Biotechnology 62: 563–571.                        evolution of desiccation tolerance in grasses. Nature Plants 10: 1112–1125.
Koster KL. 1991. Glass formation and desiccation tolerance in seeds. Plant                McGinnis LK, Zhu L, Lawitts JA, Bhowmick S, Toner M, Biggers JD. 2005.
   Physiology 96: 302–304.                                                                  Mouse sperm desiccated and stored in trehalose medium without freezing. Biology
Kranner I, Beckett R, Hochman A, Nash TH III. 2008. Desiccation-tolerance in                of Reproduction 73: 627–633.
   lichens: a review. The Bryologist 111: 576–593.                                        Mihailova G, Tchorbadjieva M, Rakleova G, Georgieva K. 2023. Differential
Kranner I, Beckett RP, Wornik S, Zorn M, Pfeifhofer HW. 2002. Revival of a                  accumulation of sHSPs isoforms during desiccation of the resurrection plant
   resurrection plant correlates with its antioxidant status: antioxidants during           Haberlea rhodopensis Friv. under optimal and high temperature. Life 13: 238.
   revival of a resurrection plant. The Plant Journal 31: 13–24.                          Montes RAC, Haber A, Pardo J, Powell RF, Divisetty UK, Silva AT, Herna ndez-
Kranner I, Birtic S. 2005. A modulating role for antioxidants in desiccation                Herna ndez T, Silveira V, Tang H, Lyons E et al. 2022. A comparative genomics
   tolerance. Integrative and Comparative Biology 45: 734–740.                              examination of desiccation tolerance and sensitivity in two sister grass species.
Leprince O, Buitink J. 2015. Introduction to desiccation biology: from old borders          Proceedings of the National Academy of Sciences, USA 119: e2118886119.
   to new frontiers. Planta 242: 369–378.                                                 Moore JP, Hearshaw M, Ravenscroft N, Lindsey GG, Farrant JM, Brandt WF.
Li J, Harper LC, Golubovskaya I, Wang CR, Weber D, Meeley RB, McElver J,                    2007. Desiccation-induced ultrastructural and biochemical changes in the leaves
   Bowen B, Cande WZ, Schnable PS. 2007. Functional analysis of maize RAD51                 of the resurrection plant Myrothamnus flabellifolia. Australian Journal of Botany
   in meiosis and double-strand break repair. Genetics 176: 1469–1482.                      55: 482.
Lin C, Jia S-N, Yang F, Jia W-H, Yu X-J, Yang J-S, Yang W-J. 2016. The                    Moore JP, Le NT, Brandt WF, Driouich A, Farrant JM. 2009. Towards a systems-
   transcription factor p8 regulates autophagy during diapause embryo formation in          based understanding of plant desiccation tolerance. Trends in Plant Science 14:
   Artemia parthenogenetica. Cell Stress & Chaperones 21: 665–675.                          110–117.
Lin C-T, Xu T, Xing S-L, Zhao L, Sun R-Z, Liu Y, Moore JP, Deng X. 2019.                  Morris JL, Puttick MN, Clark JW, Edwards D, Kenrick P, Pressel S, Wellman CH,
   Weighted gene co-expression network analysis (WGCNA) reveals the hub role of             Yang Z, Schneider H, Donoghue PCJ. 2018. The timescale of early land plant
   protein ubiquitination in the acquisition of desiccation tolerance in Boea               evolution. Proceedings of the National Academy of Sciences, USA 115: E2274–
   hygrometrica. Plant & Cell Physiology 60: 2707–2719.                                     E2283.
Liu J, Liu J, Deng L, Liu H, Liu H, Zhao W, Zhao Y, Sun X, Fan S, Wang H et al.           M€uller J, Sprenger N, Bortlik K, Boller T, Wiemken A. 1997. Desiccation increases
   2023. An intrinsically disordered region-containing protein mitigates the                sucrose levels in Ramonda and Haberlea, two genera of resurrection plants in the
   drought-growth trade-off to boost yields. Plant Physiology 192: 274–292.                 Gesneriaceae. Physiologia Plantarum 100: 153–158.
Liu S, Fang S, Cong B, Li T, Yi D, Zhang Z, Zhao L, Zhang P. 2022. The Antarctic          Nesmelov A, Cornette R, Gusev O, Kikawada T. 2018. The antioxidant system in
   moss Pohlia nutans genome provides insights into the evolution of bryophytes and         the anhydrobiotic midge as an essential, adaptive mechanism for desiccation
   the adaptation to extreme terrestrial habitats. Frontiers in Plant Science 13:           survival. Advances in Experimental Medicine and Biology 1081: 259–270.
   920138.                                                                                Neumann S, Reuner A, Br€   ummer F, Schill RO. 2009. DNA damage in storage cells
Lohaus R, Van de Peer Y. 2016. Of dups and dinos: evolution at the K/Pg boundary.           of anhydrobiotic tardigrades. Comparative Biochemistry and Physiology. Part A,
   Current Opinion in Plant Biology 30: 62–69.                                              Molecular & Integrative Physiology 153: 425–429.
Lotreck SG, Ghassemi M, VanBuren RT. 2024. Unifying the research landscape of             Nguyen K, Kc S, Gonzalez T, Tapia H, Boothby TC. 2022. Trehalose and
   desiccation tolerance to identify trends, gaps, and opportunities. bioRxiv. doi: 10.     tardigrade CAHS proteins work synergistically to promote desiccation tolerance.
   1101/2024.06.06.597802.                                                                  Communications Biology 5: 1046.
Lyall R, Schlebusch SA, Proctor J, Prag M, Hussey SG, Ingle RA, Illing N. 2020.           Nguyen K-H, Chollet-Krugler M, Gouault N, Tomasi S. 2013. UV-protectant
   Vegetative desiccation tolerance in the resurrection plant Xerophyta humilis has         metabolites from lichens and their symbiotic partners. Natural Product Reports 30:
   not evolved through reactivation of the seed canonical LAFL regulatory network.          1490–1508.
   The Plant Journal 101: 1349–1367.                                                      Nishimura N, Hitomi K, Arvai AS, Rambo RP, Hitomi C, Cutler SR, Schroeder JI,
Macovei A, Balestrazzi A, Confalonieri M, Fae M, Carbonera D. 2011. New                    Getzoff ED. 2009. Structural mechanism of abscisic acid binding and signaling by
   insights on the barrel medic MtOGG1 and MtFPG functions in relation to                   dimeric PYR1. Science 326: 1373–1379.
   oxidative stress response in planta and during seed imbibition. Plant Physiology       Nishizawa A, Yabuta Y, Shigeoka S. 2008. Galactinol and raffinose constitute a
   and Biochemistry 49: 1040–1050.                                                          novel function to protect plants from oxidative damage. Plant Physiology 147:
MacRae TH. 2016. Stress tolerance during diapause and quiescence of the brine               1251–1263.
   shrimp, Artemia. Cell Stress & Chaperones 21: 9–18.                                    Oliver MJ, Farrant JM, Hilhorst HWM, Mundree S, Williams B, Bewley JD.
Marcu D, Damian G, Cosma C, Cristea V. 2013. Gamma radiation effects                        2020. Desiccation tolerance: avoiding cellular damage during drying and
   on seed germination, growth and pigment content, and ESR study of                        rehydration. Annual Review of Plant Biology 71: 435–460.
   induced free radicals in maize (Zea mays). Journal of Biological Physics 39:           Oliver MJ, Tuba Z, Mishler BD. 2000. The evolution of vegetative desiccation
   625–634.                                                                                 tolerance in land plants. Plant Ecology 151: 85–100.
Marks RA, Delgado P, Makonya GM, Cooper K, VanBuren R, Farrant JM.                        Ooms J, Leon-Kloosterziel KM, Bartels D, Koornneef M, Karssen CM. 1993.
   2024a. Higher order polyploids exhibit enhanced desiccation tolerance                    Acquisition of desiccation tolerance and longevity in seeds of Arabidopsis thaliana
   in the grass Microchloa caffra. Journal of Experimental Botany 75:                       (a comparative study using abscisic acid-insensitive abi3 mutants). Plant
   3612–3623.                                                                               Physiology 102: 1185–1191.
Marks RA, Ekwealor JTB, Artur MAS, Bondi L, Boothby TC, Carmo OMS,                        Ostria-Gallardo E, Larama G, Berrıos G, Fallard A, Gutierrez-Moraga A,
   Centeno DC, Coe KK, Dace HJW, Field S et al. 2025a. Life on the dry side: a              Ensminger I, Bravo LA. 2020. A comparative gene co-expression analysis using
   roadmap to understanding desiccation tolerance and accelerating translational            self-organizing maps on two congener filmy ferns identifies specific desiccation
   applications. Nature Communications 16: 3284.                                            tolerance mechanisms associated to their microhabitat preference. BMC Plant
Marks RA, Farrant JM, Nicholas McLetchie D, VanBuren R. 2021a. Unexplored                   Biology 20: 56.
   dimensions of variability in vegetative desiccation tolerance. American Journal of     Pammenter NW, Berjak P. 1999. A review of recalcitrant seed physiology in
   Botany 108: 346–358.                                                                     relation to desiccation-tolerance mechanisms. Seed Science Research 9: 13–37.


Ó 2026 The Author(s).                                                                                                                New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                                             www.newphytologist.com
                                                                                                                                                                                         14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
                                                                                                                                                                     New
3174 Review             Tansley review                                                                                                                               Phytologist

     Pardo J. 2022. Evolution of drought and desiccation tolerance in grasses. East Lansing,   Richter K, Haslbeck M, Buchner J. 2010. The heat shock response: life on the verge
       MI, USA: Michigan State University.                                                        of death. Molecular Cell 40: 253–266.
     Pardo J, Man Wai C, Chay H, Madden CF, Hilhorst HWM, Farrant JM,                          Rippin M, Becker B, Holzinger A. 2017. Enhanced desiccation tolerance in mature
       VanBuren R. 2020. Intertwined signatures of desiccation and drought tolerance              cultures of the streptophytic green alga Zygnema circumcarinatum revealed by
       in grasses. Proceedings of the National Academy of Sciences, USA 117: 10079–               transcriptomics. Plant & Cell Physiology 58: 2067–2084.
       10088.                                                                                  Rizzo AM, Negroni M, Altiero T, Montorfano G, Corsetto P, Berselli P, Berra B,
     Parreira JR, Balestrazzi A, Fevereiro P, Ara ujo S d S. 2018. Maintaining genome            Guidetti R, Rebecchi L. 2010. Antioxidant defences in hydrated and desiccated
       integrity during seed development in Phaseolus vulgaris L.: evidence from a                states of the tardigrade Paramacrobiotus richtersi. Comparative Biochemistry and
       transcriptomic profiling study. Genes 9: 463.                                              Physiology. Part B, Biochemistry & Molecular Biology 156: 115–121.
     Parsell DA, Lindquist S. 1993. The function of heat-shock proteins in stress              Rodriguez MCS, Edsg€ard D, Hussain SS, Alquezar D, Rasmussen M, Gilbert T,
       tolerance: degradation and reactivation of damaged proteins. Annual Review of              Nielsen BH, Bartels D, Mundy J. 2010. Transcriptomes of the desiccation-
       Genetics 27: 437–496.                                                                      tolerant resurrection plant Craterostigma plantagineum. The Plant Journal 63:
     Peers G, Truong TB, Ostendorf E, Busch A, Elrad D, Grossman AR, Hippler M,                   212–228.
       Niyogi KK. 2009. An ancient light-harvesting protein is critical for the regulation     Roodt R, Spies JJ. 2003. Chromosome studies in the grass subfamily Chloridoideae.
       of algal photosynthesis. Nature 462: 518–521.                                              II. An analysis of polyploidy. Taxon 52: 736–746.
     Peredo EL, Cardon ZG. 2020. Shared up-regulation and contrasting down-                    Rottet S, Besagni C, Kessler F. 2015. The role of plastoglobules in thylakoid lipid
       regulation of gene expression distinguish desiccation-tolerant from intolerant             remodeling during plant development. Biochimica et Biophysica Acta 1847: 889–
       green algae. Proceedings of the National Academy of Sciences, USA 117: 17438–              899.
       17445.                                                                                  Rubinstein CV, Gerrienne P, de la Puente GS, Astini RA, Steemans P. 2010. Early
     Phillips JR, Fischer E, Baron M, van den Dries N, Facchinelli F, Kutzer M,                   middle Ordovician evidence for land plants in Argentina (eastern Gondwana):
       Rahmanzadeh R, Remus D, Bartels D. 2008. Lindernia brevidens: a novel                      rapid report. New Phytologist 188: 365–369.
       desiccation-tolerant vascular plant, endemic to ancient tropical rainforests. The       Schwab KB, Schreiber U, Heber U. 1989. Response of photosynthesis and
       Plant Journal 54: 938–948.                                                                 respiration of resurrection plants to desiccation and rehydration. Planta 177:
     Phillips JR, Hilbricht T, Salamini F, Bartels D. 2002. A novel abscisic acid- and            217–227.
       dehydration-responsive gene family from the resurrection plant Craterostigma            Sherwin HW, Farrant JM. 1998. Protection mechanisms against excess light in the
       plantagineum encodes a plastid-targeted protein with DNA-binding activity.                 resurrection plants Craterostigma wilmsii and Xerophyta viscosa. Plant Growth
       Planta 215: 258–266.                                                                       Regulation 24: 203–210.
     Pogson BJ, Albrecht V. 2011. Genetic dissection of chloroplast biogenesis and             Silva AT, Gao B, Fisher KM, Mishler BD, Ekwealor JTB, Stark LR, Li X, Zhang D,
       development: an overview. Plant Physiology 155: 1545–1551.                                 Bowker MA, Brinda JC et al. 2021. To dry perchance to live: insights from the
     Porembski S. 2007. Tropical inselbergs: habitat types, adaptive strategies and               genome of the desiccation-tolerant biocrust moss Syntrichia caninervis. The Plant
       diversity patterns. Brazilian Journal of Botany 30: 579–586.                               Journal 105: 1339–1356.
     Porembski S. 2011. Evolution, diversity, and habitats of poikilohydrous vascular          Singh SP, H€ader D-P, Sinha RP. 2010. Cyanobacteria and ultraviolet radiation
       plants. In: Bartels D, L€ uttge U, Beck E, eds. Plant desiccation tolerance. Berlin,       (UVR) stress: mitigation strategies. Ageing Research Reviews 9: 79–90.
       Heidelberg, Germany: Springer, 139–156.                                                 Smrithy V, Kulkarni A, Shigwan BK, Porembski S, Datar MN. 2023. Desiccation-
     Porembski S, Barthlott W. 2000. Granitic and gneissic outcrops (inselbergs) as               tolerant vascular plants from Western Ghats, India: review, updated checklist,
       centers of diversity for desiccation-tolerant vascular plants. Plant Ecology 151: 19–      future prospects and new insights. Nordic Journal of Botany 5: e03939.
       28.                                                                                     Sochava IV, Smirnova OI. 1993. Heat capacity of hydrated and dehydrated globular
     Porembski S, Rexroth J, Weising K, Bondi L, Mello-Silva R, Centeno DC, Datar                 proteins. Denaturation increment of heat capacity. Food Hydrocolloids 6: 513–
       MN, Watve A, Thiombano A, Tindano E et al. 2021. An overview on                            524.
       desiccation-tolerant mat-forming monocotyledons on tropical inselbergs. Flora           St Aubin B, Wai CM, Kenchanmane Raju SK, Niederhuth CE, VanBuren R.
       285: 151953.                                                                               2022. Regulatory dynamics distinguishing desiccation tolerance strategies within
     Potts M. 1994. Desiccation tolerance of prokaryotes. Microbiological Reviews 58:             resurrection grasses. Plant Direct 6: e457.
       755–805.                                                                                Tapia H, Young L, Fox D, Bertozzi CR, Koshland D. 2015. Increasing intracellular
     Potts M. 1999. Mechanisms of desiccation tolerance in cyanobacteria. European                trehalose is sufficient to confer desiccation tolerance to Saccharomyces cerevisiae.
       Journal of Phycology 34: 319–328.                                                          Proceedings of the National Academy of Sciences, USA 112: 6122–6127.
     Potts M, Slaughter SM, Hunneke F-U, Garst JF, Helm RF. 2005. Desiccation                  Tebele SM, Marks RA, Farrant JM. 2021. Two decades of desiccation biology: a
       tolerance of prokaryotes: application of principles to human cells. Integrative and        systematic review of the best studied angiosperm resurrection plants. Plants 10:
       Comparative Biology 45: 800–809.                                                           2784.
     Proctor MCF, Oliver MJ, Wood AJ, Alpert P, Stark LR. 2007. Desiccation-                   Tibiletti T, Auroy P, Peltier G, Caffarri S. 2016. Chlamydomonas reinhardtii PsbS
       tolerance in bryophytes: a review. The Bryologist 110: 595–621.                            protein is functional and accumulates rapidly and transiently under high light.
     Proctor MCF, Tuba Z. 2002. Poikilohydry and homoihydry: antithesis or spectrum               Plant Physiology 171: 2717–2730.
       of possibilities? New Phytologist 156: 327–349.                                         Toth S, Kiss C, Scott P, Kova cs G, Sorvari S, Toldi O. 2006. Agrobacterium-
     Rafsanjani A, Brule V, Western TL, Pasini D. 2015. Hydro-responsive                         mediated genetic transformation of the desiccation tolerant resurrection plant
       curling of the resurrection plant Selaginella lepidophylla. Scientific Reports 5:          Ramonda myconi (L.) Rchb. Plant Cell Reports 25: 442–449.
       8064.                                                                                   Tuba Z, Lichtenthaler HK. 2011. Ecophysiology of homoiochlorophyllous and
     Rastogi RP, Sonani RR, Madamwar D. 2015. Cyanobacterial sunscreen                            poikilochlorophyllous desiccation-tolerant plants and vegetations. In: Ecological
       scytonemin: role in photoprotection and biomedical research. Applied                       studies: analysis and synthesis. Berlin, Heidelberg, New York. Plant desiccation
       Biochemistry and Biotechnology 176: 1551–1563.                                             tolerance. Berlin, Heidelberg, Germany: Springer Berlin Heidelberg, 157–183.
     Ratnakumar S, Hesketh A, Gkargkas K, Wilson M, Rash BM, Hayes A,                          Tuba Z, Protor CF, Csintalan Z. 1998. Ecophysiological responses of
       Tunnacliffe A, Oliver SG. 2011. Phenomic and transcriptomic analyses reveal                homoiochlorophyllous and poikilochlorophyllous desiccation tolerant plants: a
       that autophagy plays a major role in desiccation tolerance in Saccharomyces                comparison and an ecological perspective. Plant Growth Regulation 24: 211–217.
       cerevisiae. Molecular BioSystems 7: 139–149.                                            Tunnacliffe A, Wise MJ. 2007. The continuing conundrum of the LEA proteins.
     Rebecchi L. 2013. Dry up and survive: the role of antioxidant defences in                    The Science of Nature 94: 791–812.
       anhydrobiotic organisms. Journal of Limnology 72: 62–72.                                Tyson T, O’Mahony Zamora G, Wong S, Skelton M, Daly B, Jones JT, Mulvihill
     Reina-Bueno M, Argando~      na M, Nieto JJ, Hidalgo-Garcıa A, Iglesias-Guerra F,           ED, Elsworth B, Phillips M, Blaxter M et al. 2012. A molecular analysis of
       Delgado MJ, Vargas C. 2012. Role of trehalose in heat and desiccation tolerance            desiccation tolerance mechanisms in the anhydrobiotic nematode Panagrolaimus
       in the soil bacterium Rhizobium etli. BMC Microbiology 12: 207.                            superbus using expressed sequenced tags. BMC Research Notes 5: 68.


     New Phytologist (2026) 251: 3159–3175                                                                                                              Ó 2026 The Author(s).
     www.newphytologist.com                                                                                                 New Phytologist Ó 2026 New Phytologist Foundation.
                                                                                                                                                                                   14698137, 2026, 6, Downloaded from https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.71466 by Capes, Wiley Online Library on [28/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
New
Phytologist                                                                                                                                  Tansley review           Review 3175


Vaidya AS, Helander JDM, Peterson FC, Elzinga D, Dejonghe W, Kaundal A,                   Wise MJ, Tunnacliffe A. 2004. POPP the question: what do LEA proteins do?
  Park S-Y, Xing Z, Mega R, Takeuchi J et al. 2019. Dynamic control of plant                Trends in Plant Science 9: 13–17.
  water use using designed ABA receptor agonists. Science 366: eaaw8848.                  Wolkers WF, McCready S, Brandt WF, Lindsey GG, Hoekstra FA. 2001. Isolation
VanBuren R, Bryant D, Edger PP, Tang H, Burgess D, Challabathula D, Spittle K,              and characterization of a D-7 LEA protein from pollen that stabilizes glasses in
  Hall R, Gu J, Lyons E et al. 2015. Single-molecule sequencing of the desiccation-         vitro. Biochimica et Biophysica Acta 1544: 196–206.
  tolerant grass Oropetium thomaeum. Nature 527: 508–511.                                 Wolkers WF, Oldenhof H, Alberda M, Hoekstra FA. 1998. A Fourier
VanBuren R, Man Wai C, Pardo J, Giarola V, Ambrosini S, Song X, Bartels D.                  transform infrared microspectroscopy study of sugar glasses: application
  2018a. Desiccation tolerance evolved through gene duplication and network                 to anhydrobiotic higher plant cells. Biochimica et Biophysica Acta 1379: 83–
  rewiring in Lindernia. Plant Cell 30: 2943–2958.                                          96.
VanBuren R, Pardo J, Man Wai C, Evans S, Bartels D. 2019. Massive tandem                  Womersley C. 1981. Biochemical and physiological aspects of anhydrobiosis.
  proliferation of ELIPs supports convergent evolution of desiccation tolerance             Comparative Biochemistry and Physiology Part B: Comparative Biochemistry 70:
  across land plants. Plant Physiology 179: 1040–1049.                                      669–678.
VanBuren R, Wai CM, Giarola V, Zupunski         M, Pardo J, Kalinowski M,                Wood AJ. 2007. The nature and distribution of vegetative desiccation-tolerance in
  Grossmann G, Bartels D. 2023. Core cellular and tissue-specific mechanisms                hornworts, liverworts and mosses. The Bryologist 110: 163–177.
  enable desiccation tolerance in Craterostigma. The Plant Journal 114: 231–245.          Wright DJ, Smith SC, Joardar V, Scherer S, Jervis J, Warren A, Helm RF, Potts M.
VanBuren R, Wai CM, Keilwagen J, Pardo J. 2018b. A chromosome-scale assembly                2005. UV irradiation and desiccation modulate the three-dimensional
  of the model desiccation tolerant grass Oropetium thomaeum. Plant Direct 2:               extracellular matrix of Nostoc commune (Cyanobacteria). The Journal of Biological
  e00096.                                                                                   Chemistry 280: 40271–40281.
VanBuren R, Wai CM, Ou S, Pardo J, Bryant D, Jiang N, Mockler TC, Edger P,                Wright PE, Dyson HJ. 2015. Intrinsically disordered proteins in cellular signalling
  Michael TP. 2018c. Extreme haplotype variation in the desiccation-tolerant                and regulation. Nature Reviews. Molecular Cell Biology 16: 18–29.
  clubmoss Selaginella lepidophylla. Nature Communications 9: 13.                         Xiao B, Huang Y, Tang N, Xiong L. 2007. Over-expression of a LEA gene in rice
VanBuren R, Wai CM, Zhang Q, Song X, Edger PP, Bryant D, Michael TP,                        improves drought resistance under the field conditions. Theoretical and Applied
  Mockler TC, Bartels D. 2017. Seed desiccation mechanisms co-opted for                     Genetics 115: 35–46.
  vegetative desiccation in the resurrection grass Oropetium thomaeum. Plant, Cell &      Xiao L, Yang G, Zhang L, Yang X, Zhao S, Ji Z, Zhou Q, Hu M, Wang Y, Chen M
  Environment 40: 2292–2306.                                                                et al. 2015. The resurrection genome of Boea hygrometrica: a blueprint for survival
Vander Willigen C, Pammenter NW, Mundree S, Farrant J. 2001. Some                           of dehydration. Proceedings of the National Academy of Sciences, USA 112: 5833–
  physiological comparisons between the resurrection grass, Eragrostis nindensis,           5837.
  and the related desiccation-sensitive species, E. curvula. Plant Growth Regulation      Xu H-F, Dai G-Z, Bai Y, Shang J-L, Zheng B, Ye D-M, Shi H, Kaplan A, Qiu B-S.
  35: 121–129.                                                                              2022. Coevolution of tandemly repeated hlips and RpaB-like transcriptional
Vanschoenwinkel B, de Paula LFA, Snoeks JM, Van der Stocken T, Buschke FT,                  factor confers desiccation tolerance to subaerial Nostoc species. Proceedings of the
  Porembski S, Silveira FAO. 2025. The ecological and evolutionary dynamics of              National Academy of Sciences, USA 119: e2211244119.
  inselbergs. Biological Reviews of the Cambridge Philosophical Society 100: 481–507.     Xu Z, Xin T, Bartels D, Li Y, Gu W, Yao H, Liu S, Yu H, Pu X, Zhou J et al. 2018.
de Vries J, Archibald JM. 2018. Plant evolution: landmarks on the path to terrestrial       Genome analysis of the ancient tracheophyte Selaginella tamariscina reveals
  life. New Phytologist 217: 1428–1434.                                                     evolutionary features relevant to the acquisition of desiccation tolerance.
Walters C, Hill LM, Wheeler LJ. 2005. Dying while dry: kinetics and mechanisms              Molecular Plant 11: 983–994.
  of deterioration in desiccated organisms. Integrative and Comparative Biology 45:       Yu J, Lai Y, Wu X, Wu G, Guo C. 2016. Overexpression of OsEm1 encoding a
  751–758.                                                                                  group I LEA protein confers enhanced drought tolerance in rice. Biochemical and
Wang Y, Jiang J, Zhao X, Liu G, Yang C, Zhan L. 2006. A novel LEA gene from                 Biophysical Research Communications 478: 703–709.
  Tamarix androssowii confers drought tolerance in transgenic tobacco. Plant              Yu J, Li L, Wang S, Dong S, Chen Z, Patel N, Goffinet B, Chen H, Liu H, Liu Y.
  Science 171: 655–662.                                                                     2020. Draft genome of the aquatic moss Fontinalis antipyretica (Fontinalaceae,
Wang Y, Zhu L, Yang Y, Li X, Zhang X, Fang X. 2026. Cellular water-potential                Bryophyta). GigaByte 2020: gigabyte8.
  sensing through biomolecular condensation. Nature. doi: 10.1038/s41586-026-             Zamecnik J, Faltus M, Bilavcik A. 2021. Vitrification solutions for plant
  10591-8.                                                                                  cryopreservation: Modification and properties. Plants 10: 2623.
Watanabe M. 2006. Anhydrobiosis in invertebrates. Applied Entomology and Zoology          Zhang Q, Song X, Bartels D. 2016. Enzymes and metabolites in carbohydrate
  41: 15–31.                                                                                metabolism of desiccation tolerant plants. Proteomes 4: 40.
Waterworth WM, Bray CM, West CE. 2019. Seeds and the art of genome                        Zhang X, Ekwealor JTB, Mishler BD, Silva AT, Yu L, Jones AK, Nelson ADL,
  maintenance. Frontiers in Plant Science 10: 706.                                          Oliver MJ. 2024. Syntrichia ruralis: emerging model moss genome reveals a
Wehmeyer N, Vierling E. 2000. The expression of small heat shock proteins in seeds          conserved and previously unknown regulator of desiccation in flowering plants.
  responds to discrete developmental signals and suggests a general protective role in      New Phytologist 243: 981–996.
  desiccation tolerance. Plant Physiology 122: 1099–1108.                                 Zhuo C, Cai J, Guo Z. 2013. Overexpression of early light-induced protein (ELIP)
Whittaker A, Bochicchio A, Vazzana C, Lindsey G, Farrant J. 2001. Changes in leaf           gene from Medicago sativa ssp. falcata increases tolerance to abiotic stresses.
  hexokinase activity and metabolite levels in response to drying in the desiccation-       Agronomy Journal 105: 1433–1440.
  tolerant species Sporobolus stapfianus and Xerophyta viscosa. Journal of Experimental   Zia A, Walker BJ, Oung HMO, Charuvi D, Jahns P, Cousins AB, Farrant JM,
  Botany 52: 961–969.                                                                       Reich Z, Kirchhoff H. 2016. Protection of the photosynthetic apparatus against
Whittaker A, Martinelli T, Farrant JM, Bochicchio A, Vazzana C. 2007. Sucrose               dehydration stress in the resurrection plant Craterostigma pumilum. The Plant
  phosphate synthase activity and the co-ordination of carbon partitioning during           Journal 87: 664–680.
  sucrose and amino acid accumulation in desiccation-tolerant leaf material of the
  C4 resurrection plant Sporobolus stapfianus during dehydration. Journal of              Disclaimer: The New Phytologist Foundation remains neutral with regard to
  Experimental Botany 58: 3775–3787.                                                      jurisdictional claims in maps and in any institutional affiliations.
Williams B, Njaci I, Moghaddam L, Long H, Dickman MB, Zhang X, Mundree S.
  2015. Trehalose accumulation triggers autophagy during plant desiccation. PLoS
  Genetics 11: e1005705.




Ó 2026 The Author(s).                                                                                                                New Phytologist (2026) 251: 3159–3175
New Phytologist Ó 2026 New Phytologist Foundation.                                                                                             www.newphytologist.com
