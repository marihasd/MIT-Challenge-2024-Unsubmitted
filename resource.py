class Resource:
    def __init__(self, name, location, services_offered, additional_criteria):
        """
        Represents a resource with essential attributes.

        Args:
        - name (str): Name of the resource.
        - location (str): Location of the resource.
        - services_offered (list of str): Services offered by the resource.
        - additional_criteria (dict): Additional criteria for matching.

        Attributes:
        - relevance_score (int): Score indicating relevance to user needs.
        """
        self.name = name
        self.location = location
        self.services_offered = services_offered
        self.additional_criteria = additional_criteria
        self.relevance_score = 0

def resource_matches_needs(resource, individual_needs):
    """
    Checks if a resource matches individual needs based on services offered and additional criteria.

    Args:
    - resource (Resource): Resource object to check.
    - individual_needs (dict): Individual's specific needs.

    Returns:
    - bool: True if resource matches needs, False otherwise.
    """
    if any(service in resource.services_offered for service in individual_needs['challenges']):
        if meets_additional_criteria(resource, individual_needs):
            return True
    return False

def meets_additional_criteria(resource, individual_needs):
    """
    Checks if a resource meets additional criteria like location and eligibility.

    Args:
    - resource (Resource): Resource object to check.
    - individual_needs (dict): Individual's specific needs.

    Returns:
    - bool: True if resource meets additional criteria, False otherwise.
    """
    if 'location' in resource.additional_criteria and resource.location != individual_needs['location']:
        return False
    if 'eligibility' in resource.additional_criteria and resource.additional_criteria['eligibility'] != individual_needs['eligibility']:
        return False
    # Add more specific criteria checks as needed
    return True

def rank_resources(matched_resources):
    """
    Ranks matched resources based on relevance score.

    Args:
    - matched_resources (list of Resource): List of resources to rank.

    Returns:
    - list of Resource: Ranked list of resources.
    """
    ranked_resources = sorted(matched_resources, key=lambda x: x.relevance_score, reverse=True)
    return ranked_resources

def calculate_relevance_score(resource, individual_needs):
    """
    Calculates relevance score for a resource based on factors like location.

    Args:
    - resource (Resource): Resource object to calculate score for.
    - individual_needs (dict): Individual's specific needs.
    """
    score = 0
    if resource.location == individual_needs['location']:
        score += 1
    # Add more factors (proximity, services match, etc.) to calculate score
    resource.relevance_score = score
