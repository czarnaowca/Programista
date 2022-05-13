from stix2 import Malware
from stix2 import Identity
from stix2 import Infrastructure
from stix2 import ThreatActor
from stix2 import IPv4Address
from stix2 import Bundle
from stix2 import Relationship
from stix2.v21.vocab import INFRASTRUCTURE_TYPE_COMMAND_AND_CONTROL


def produce_stix():
    """
    Produce sample Bundle object with STIX definition
    :return: Bundle
    """
    threat_actor = ThreatActor(name="Sample Threat "
                                    "Actor Group",
                               description=
                               "This organized threat "
                               "actor group use Cobalt "
                               "Strike framework",
                               sophistication="expert",
                               resource_level="organization",
                               primary_motivation=
                               "personal-gain")

    sample_team = Identity(name="Sample Team",
                           description="Sample Team is "
                                       "the name of an "
                                       "organized threat"
                                       " actor "
                                       "crime-syndicate.",
                           identity_class="organization")

    # Relationship between Sample Team
    # and Sample Threat Actor Group
    sample_team_threat_actor_rel = Relationship(
        threat_actor, "attributed-to", sample_team)

    malware_cobalt = Malware(name="Cobalt Strike Beacon",
                             is_family=True)

    c2_infrastructure = Infrastructure(
        name="Cobalt Strike C2 server",
        infrastructure_types=
        INFRASTRUCTURE_TYPE_COMMAND_AND_CONTROL)

    # Relationship between Sample Threat Actor Group
    # and C2 infrastructure
    threat_actor_infra_rel = Relationship(threat_actor,
                                          "owns",
                                          c2_infrastructure)

    c2_ip_1 = IPv4Address(value="5.181.86.243")
    c2_ip_2 = IPv4Address(value="51.83.253.56")

    # Relationships between C2 infrastructure
    # and IP addresses
    c2_ip_1_infra_rel = Relationship(c2_infrastructure,
                                     "consist-of", c2_ip_1)
    c2_ip_2_infra_rel = Relationship(c2_infrastructure,
                                     "consist-of", c2_ip_2)

    # Relationship between Cobalt Strike Beacon
    # and C2 infrastructure
    malware_infra_rel = Relationship(c2_infrastructure,
                                     "controls",
                                     malware_cobalt)

    return Bundle([threat_actor, sample_team,
                   sample_team_threat_actor_rel,
                   threat_actor_infra_rel, malware_cobalt,
                   c2_infrastructure, c2_ip_1, c2_ip_2,
                   c2_ip_1_infra_rel, c2_ip_2_infra_rel,
                   malware_infra_rel])


if __name__ == "__main__":
    print(produce_stix().serialize(pretty=True))
