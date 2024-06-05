

# Affordances Axiomatization

We decided to focus on 5 affordances in particular:
Containment,  
Grasping,  
Pouring,  
Cutting,  
Stabbing



### Containment refined


**Containment Situation Definition:**
    $$∀o1,o2:Containment(o1,o2)→(∃c:Container(o1)∧Containee(o2)∧Interior(o1,o2)∧Inside(o2,o1))\forall o1, o2 : Containment(o1, o2) \rightarrow (\exists c : Container(o1) \wedge Containee(o2) \wedge InteriorSpace(o1, o2) \wedge Inside(o2, o1)))$$
    
    **Explanation:** If there is a containment situation Containment(o1,o2), then o1 is a :Container, o2 is a :Containee, and o2 is :inside the :Interior of o1.
    
**Interior and Boundary Relationship:**
    $$∀o1,o2:Container(o1)∧Containee(o2)∧Inside(o2,o1)→(∃b:Boundary(b)∧defines(b,InteriorSpace(o1,o2)))$$
    
    **Explanation:** If o1 is a :Container and o2 is a :Containee inside o1, then there exists a :Boundary b that defines the :Interior space of o1.
    
**Contact and Containment:**
    
    $$∀o1,o2:Container(o1)∧Containee(o2)∧Inside(o2,o1)→(∃c:ContactSituation(c)∧hasPrtcp(c,o1)∧hasPrtcp(c,o2))$$
    **Explanation:** If o1 is a :Container and o2 is a :Containee :inside o1, then there is :ContactSituation taking as participants o1 and o2.
    
**Force Exertion in Containment:**
    
    $$∀f,o1,o2:aff(f,o2)∧Inside(o2,o1)→(∃o3:exrt(o3,f)∧dir(f,inward))$$
    **Explanation:** If a :Force f :affects a :Containee o2 that is :inside a :Container o1, then there exists another :Object o3 that :exerts f with a :Direction inward :towards the :Interior of o1.
    
**Containment Implies Spatial Relationship:**
    
    $$∀o1,o2:Containment(o1,o2)→Inside(o2,o1)$$
    
    **Explanation:** If a :Containment situation Containment(o1,o2) exists, then the :Containee o2 is :inside the :Container o1.
    
**Typical Objects and Containment:**
    $$∀o:Containee(o)→(∃f:exrt(floor,f)∧Grv(f)∧aff(f,o))$$
    
    **Explanation:** For all :Containees o, there exists a :Force f exerted by the floor that affects o due to :Gravity.
    
**Non-movement Due to Containment:**
    (useful for strange cases of "not falling objects" maybe...?)
    $$∀o,f,d:Containee(o)∧aff(f,o)∧dir(f,d)∧¬movDir(o,d)→(∃o1:Container(o1)∧Inside(o,o1))$$
    
    **Explanation:** If a :Containee o is affected by a :Force f in :Direction d and does not move in :Direction d, then there exists a :Container o1 such that o is :inside o1.


**Localization Relationship in Interior:**
    
    $$∀o1,o2:Container(o1)∧Containee(o2)→(∃i:InteriorSpace(i,o1)∧localisedIn(o2,i))$$
    
    **Explanation:** If o1 is a :Container and o2 is a :Containee, then there exists an :InteriorSpace i of o1 such that o2 is :localisedIn i.
    
**Boundary Defines Interior:**
    
    $$∀o1,i:Container(o1)∧InteriorSpace(i,o1)→(∃b:Boundary(b)∧defines(b,i))$$
    
    **Explanation:** If o1 is a :Container and has an :InteriorSpace i, then there exists a :Boundary b that :defines i.


In addition to this some more trivial axioms:

$$∀o:Container(o)→(Object(o)$$
**Explanation**:
Each :Container o is an :Object o.

This could be useful to predicate something for generic Objects and not repeat the axioms for all the subclasses of objects.


### Grasping refined:

**Grasping Situation Definition:**
    
    $$∀o1,o2:Grasping(o1,o2)→(∃g:GraspingSituation(g)∧Grasper(o1)∧GraspedObject(o2)∧ContactSituation(c)∧hasPrtc(c,o1)∧hasPartc(c,o2)∧Grip(o1,o2)∧Stability(o2))$$
    
**Explanation:** If there is a :GraspingSituation g, which :hasParticipant o1 and o2, and o2 is :grasping o2, then o1 is a :Grasper, o2 is a GraspedObject, and there is a :ContactSituation which :hasParticipant o1 and o2, and o1 exerts some grip on o2, and o2 has some :Stability.
    
**Force Exertion in Grasping:**
    $$∀f,o1,o2:aff(f,o2)∧Contact(o1,o2)→(∃o3:exrt(o3,f)∧dir(f,hold))$$
    
**Explanation:** If a :Force f :affects a :GraspedObject o2 that is in :Contact with a :Grasper o1, then there exists another :Object o3 that exerts f with a :Direction to hold o2. (holding means GraspingSituation + Stability of o2)

Corollarium axiom: Stability
Stability is different from Immobility since Stability is the Situation for which a certain Object o is stable when e.g. supported, grasped, lifted, etc. namely there is no :Movement detected at t2 for an :Object which at t1 was :Containee, :Supported, :GraspedObject, :LiftedObject etc.
    
**Contact and Grasping:**
    
    $$∀o1,o2,f:Grasper(o1)∧exrt(o1,f)∧aff(f,o2)∧dir(f,hold)→(∃c:ContactSituation(c)∧hasPrtcp(o1)∧hasPrtcp(o2)∧GraspingPoint(o2,c))$$
    
**Explanation:** If a :Grasper o1 :exerts a :Force f that :affects a :GraspedObject o2o with a :Direction to :hold, then o1 and o2 are in a :ContactSituation at a specific :GraspingPoint.
    
**Grasping Implies Contact Relationship:**
    
    $$∀o1,o2:GraspingSituation(o1,o2)→ContactSituation(o1,o2)$$
    
**Explanation:** Each :GraspingSituation implies a :ContactSituation
    
**Typical Objects and Grasping:**
    
    $$∀o:GraspedObject(o)→(∃f:exrt(floor,f)∧Grv(f)∧aff(f,o))$$
    
**Explanation:** For all :GraspedObjects o, there exists a :Force f :exerted by the :Floor that ;affects o due to :Gravity.
    
**Grip Force and Stability:**
    
    $$∀o1,o2,f:Grasper(o1)∧GraspedObject(o2)∧aff(f,o2)∧dir(f,hold)∧Stability(o2)→Grip(o1,o2)$$
    
**Explanation:** If a Grasper o1 applies a :Force f to :hold a :GraspedObject o2 and o2 has at t2 a certain :Stability, then o1 has a :Grip on o2.
    

**Contact and Grasping Points:**
    
    $$∀o1,o2:Contact(o1,o2)→(∃gp:GraspingPoint(gp)∧hasPrtcp(gp, o1)∧hasPrtcp(gp, o2)$$
    
**Explanation:** If there is contact between a :Grasper o1 and a :GraspedObject o2, then there exists a :GraspingPoint gp that :hasParticipant o1 and o2.



### Pouring refined

**Pouring Situation Definition:**
    
    $$∀o1,l,s,t, ps:PouringSituation(ps)∧hasPrtcp(o1)∧hasPrtcp(l)∧hasPrtcp(s)∧hasPrtcp(t)→(∃p:Pourer(o1)∧Liquid(l)∧SourceContainer(s)∧TargetContainer(t)∧FlowsFrom(l,s,t))$$
    
**Explanation:** If there is a :PouringSituation ps then it takes as participants o1 as a :Pourer, l as a :Liquid, s as a :SourceContainer, t as a :TargetContainer, and l :flowsFrom s to t.

Corollarium: let's introduce the axiomatisation for "sequence".
A Sequence sq is a concatenation of at least 2 situations s1 and s2, where s1 is temporalised at t1 and s2 at t2. Let's assume that s1 is the :InitialState and s2 is the :FinalState

$$∀sq,s1,s2,t1,t2 :SequenceSituation(sq)∧hasInitialState(s1)∧hasFinalState(s2)∧happensAtTime(s1,t1)∧happensAtTime(s2,t2)$$

For example, a PouringSituation involves two containment situations as InitialState and FinalState, both taking as participants the same liquid, but involving different :SourceContainer and :TargetContainer .

**Containment in Source and Target Containers:**
    $$∀ps, c1, c2, l, sc, tc, t1, t2: PouringSequence(ps)∧ContainmentSituation(s1)∧ContainmentSituation(s2)Liquid(l)∧SourceContainer(sc)∧TargetContainer(tc)∧Time(t1)∧Time(t2)→hasPrtcp(c1, (sc,l))∧hasPrtcp(c2, (tc,l))∧happensAtTime(c1,t1)∧happensAtTime(c2,t2)$$
    
    
**Flow and Direction in Pouring:**
    
    $$∀f,l,s,t:Flow(f,s,t)∧Liquid(l)→(∃d:exrt(s,f)∧dir(f,d)∧d=downward)$$
    
**Explanation:** If there is a :Flow f of a :Liquid l from a :SourceContainer s to a :TargetContainer t, then s :exerts f in a :downward :Direction.
    
**Force Exertion in Pouring:**
    
    $$∀f,l,s,t:Flow(f,s,t)∧Liquid(l)→(∃o1:Pourer(o1)∧exrt(o1,f)∧dir(f,down))$$

**Explanation:** If there is a :Flow f of a :Liquid l from a :SourceContainer s to a :TargetContainer t, then there exists a :Pourer o1 that :exerts f with a :downward :Direction.
    
**Pouring Implies Movement of Liquid:**
    
    $$∀o1,l,s,t:PouringSituation(o1,l,s,t)→(∃f:Flow(f,s,t)∧Movement(l,downward))$$
    
**Explanation:** If there is a :PouringSituation then there exists a :Flow f from the :SourceContainer s to the :TargetContainer t and a :downward :Movement of the Liquid l.
    
**Contact and Pouring:**
    $$∀o1,l,s,t:Pourer(o1)∧Liquid(l)∧SourceContainer(s)∧TargetContainer(t)∧Flow(l,s,t)→(∃c1,c2,c3:ContactSituation(c1)∧ContactSituation(c2)∧ContactSituation(c3)∧hasPrtcp(c1,o1)∧hasPrtcp(c1,l)∧hasPrtcp(c2,s)∧hasPrtcp(c2,l)∧hasPrtcp(c3,l)∧hasPrtcp(c3,t))$$
    
**Explanation:** If o1 is a :Pourer, l is a :Liquid, s is a :SourceContainer, and t is a :TargetContainer with :Flow from s to t, then: there is :Contact between the :Pourer and the :Liquid; between the Liquid and the :SourceContainer, and between the :Liquid and the :TargetContainer.

Note that Contact in this case is not a transitive relation.

### Cutting refined

**Cutting Situation Definition:**
    
    $$∀o1,t,o2:Cutting(o1,t,o2)→(∃c:Cutter(o1)∧CuttingTool(t)∧Cuttee(o2)∧Contact(t,o2)∧Cut(o2))$$
    
**Explanation:** If there is a :CuttingSituation, then o1 is a :Cutter, t is a :CuttingTool, o2 is a :Cuttee, and there is :Contact between t and o2, resulting in a :Cut in o2.

The next one probably is not necessary, but still:
**Force Exertion in Cutting:**
    
    $$∀f,t,o2:aff(f,o2)∧Contact(t,o2)→(∃o1:Cutter(o1)∧exrt(o1,f))$$
    
**Explanation:** If a :Force f affects a :Cuttee o2 that is in :Contact with a :CuttingTool t, then there exists a :Cutter o1 that :exerts f .
    
**Contact and Cutting:**
    
    $$∀o1,t,o2,f:Cutter(o1)∧exrt(o1,f)∧aff(f,o2)→(∃c:Contact(c)∧hasPrtcp(t)∧hasPrtcp(o2)∧CuttingPoint(o2,c))$$
    
**Explanation:** If a :Cutter o1 :exerts a :Force f that :affects a :Cuttee o2, then t and o2 are in contact at a specific :CuttingPoint.
    
**Cutting Implies Contact Relationship:**
    
    $$∀o1,t,o2:CuttingSituation(o1,t,o2)→Contact(t,o2)$$
    
**Explanation:** If a Cutter o1 :cuts a :Cuttee o2 using a :CuttingTool t, then t is in :contact with o2.
    
**Objects and Cutting:**
    
    $$∀o:Cuttee(o)→Object(o)$$
    
**Explanation:** For all Cuttees o, they are also Objects. This imply e.g. that they are subject to :Gravity, etc.
    
**Cutting Results in Separation:**
    
    $$∀o1,t,o2:CuttingSituation(o1,t,o2)→(∃s1,s2:partOf(s1,o2)∧partOf(s2,o2)∧Separated(s1,s2)∧Object(o1)∧Object(o2))$$
    
**Explanation:** If there is a :CuttingSituation, then the Cuttee o2 results in parts s1 and s2 that are separated :Objects.
    

 **Part-Whole Relationship in Cutting:**
    
    $$∀o2,s1,s2:Cuttee(o2)→(∃s1,s2:partOf(s1,o2)∧partOf(s2,o2)∧Separated(s1,s2))$$
    
**Explanation:** If o2 is a :Cuttee, then there exist :Parts s1 and s2 of o2 that are separated as a result of a CuttingSituation.
    
**Contact and Cutting Points:**
    
 $$   ∀t,o2:Contact(t,o2)→(∃cp:CuttingPoint(cp,o2)∧partOf(cp,o2))$$
    
**Explanation:** If there is contact between a :CuttingTool t and a :Cuttee o2, then there exists a :CuttingPoint cp that is part of o2.



### Stabbing refined


**Stabbing Situation Definition:**
    
    $$∀o1,t,o2:Stabbing(o1,t,o2)→(∃s:Stabber(o1)∧StabbingTool(t)∧Stabbee(o2)∧Contact(t,o2)∧Penetration(t,o2))$$
    
**Explanation:** If there is a :StabbingSituation, then o1 is a :Stabber, t is a :StabbingTool, o2 is a :Stabbee, and there is contact and penetration involved.
This imply of course that stabbing is the combination of a ContactSituation and PenetrationSituation.

    
**Contact and Stabbing:**
    
    $$∀o1,t,o2,f:Stabber(o1)∧exrt(o1,f)∧aff(f,o2)→(∃c:Contact(c)∧hasPrtcp(t)∧hasPrtcp(o2)∧StabbingPoint(o2,c))$$
    
**Explanation:** If a :Stabber o1 :exerts a :Force f that :affects a :Stabbee o2, then t and o2 are in contact at a specific :StabbingPoint.
    
**Stabbing Implies Contact Relationship:**
    
    $$∀o1,t,o2:Stabbing(o1,t,o2)→Contact(t,o2)$$
    
**Explanation:** If a :Stabber o1 :stabs a :Stabbee o2 using a :StabbingTool t, then t is in :contact with o2.
    
**Objects and Stabbing:**
    
    $$∀o:Stabbee(o)→Object(o)$$
    
**Explanation:** As always, inherit general world axioms like :Gravity.
    
**Stabbing Results in Penetration:**
    
    $$∀o1,t,o2:Stabbing(o1,t,o2)→(∃p:Penetration(p,t,o2)∧ContainedPart(p,t,o2))$$
    
**Explanation:** If there is a StabbingSituation, then the :StabbingTool t :penetrates the :Stabbee o2 and a :Part of t is :contained within o2.


**Part-Whole Relationship in Stabbing:**
    
    $$∀o2,p,t:PenetrationSituation(p,t,o2)→(∃cp:ContainedPart(cp,t,o2)∧partOf(cp,t)∧Inside(cp,o2))$$
    
**Explanation:** If p is a :PenetrationSituation of a :StabbingTool t into a :Stabbee o2, then there exists a ContainedPart cp of t that is :inside o2.
    
**Contact and Stabbing Points:**
    
    $$∀t,o2:Contact(t,o2)→(∃sp:StabbingPoint(sp,o2)∧partOf(sp,o2))$$
    
**Explanation:** If there is contact between a :StabbingTool t and a :Stabbee o2, then there exists a :StabbingPoint sp that is part of o2.
Now, this is true since a :StabbingTool is as such as long as it is part of a :StabbingSituation, therefore this should not imply that all the times that e.g. we have a fork and an apple in contact we have a :StabbingSituation, but this implies that, if we have a :StabbingSituation and a fork satisfying the role of :Stabber, then there is contact between the :StabbingTool and the :Stabbee .
    
**Containment in Penetration:**
    
    $$∀t,o2:Penetration(t,o2)→Containment(o2,t)$$
    
**Explanation:** If there is a :PenetrationSituation of a :StabbingTool t into a :Stabbee o2, then o2 contains part of t.
