Here’s a more polished version of your introduction to dictionaries content:

---

# Introduction to Dictionaries (Part 2)

Dictionaries are particularly useful for representing structured and related data. The example below demonstrates a more
realistic "ticket" from popular ticketing software, **Jira**.

Take a look:

![Jira Ticket](https://d17h27t6h515a5.cloudfront.net/topher/2017/November/59fb6ccd_jira-ticket/jira-ticket.png)

### Example: Representing a Ticket in a Dictionary

```python
# The structure of a Jira ticket is captured in this dictionary
ticket = {
    "type": "bug",
    "status": "done",
    "priority": "medium",
    "resolution": "done",
    "description": "testing 123",
    "attachments": [],
    "people": {
        "assignee": None,
        "reporter": {
            "name": "Andy Brown",
            "image": "www.example_image_url.com"
        },
        "votes": 0,
        "watchers": [
            {
                "name": "Andy Brown",
                "image": "www.example_image_url.com"
            }
        ]
    },
    "dates": {
        "created": "6 days ago",
        "updated": "6 days ago",
        "resolved": "6 days ago"
    }
}

# Display the keys in the dictionary
print("The keys for this dictionary are...")
print(ticket.keys())
```

Output:

```plaintext
The keys for this dictionary are...
dict_keys(['type', 'status', 'priority', 'resolution', 'description', 'attachments', 'people', 'dates'])
```

The dictionary `ticket` organizes all the information about a Jira ticket, such as its type, status, priority, and the
people involved.

```python
# Accessing the reporter's name in the dictionary
ticket['people']['reporter']['name']
```

Output:

```plaintext
'Andy Brown'
```

### Working with a List of Tickets

Let’s pull in some sample data, representing multiple tickets:

```python
from sample_data import big_tickets
import random

print("There are", len(big_tickets), "tickets in the dataset.")
```

Output:

```plaintext
There are 250 tickets in the dataset.
```

Now, let's grab a random ticket and inspect its structure:

```python
# Select and display a random ticket
random_ticket = random.choice(big_tickets)
print(random_ticket)
```

A sample ticket might look like this:

```plaintext
{
  'type': 'bug',
  'status': 'done',
  'priority': 'medium',
  'resolution': 'done',
  'description': 'testing 123',
  'attachments': [],
  'people': {
    'assignee': None,
    'reporter': {
      'name': 'Erika Alonzo',
      'image': 'www.example_image_url.com'
    },
    'votes': 0,
    'watchers': [
      {'name': 'Cezanne Camacho', 'image': 'www.example_image_url.com'},
      {'name': 'Andrew Paster', 'image': 'www.example_image_url.com'},
      {'name': 'Jonathan Sullivan', 'image': 'www.example_image_url.com'},
      {'name': 'Anthony Navarro', 'image': 'www.example_image_url.com'},
      {'name': 'Kagure Kabue', 'image': 'www.example_image_url.com'},
      {'name': 'Sebastian Thrun', 'image': 'www.example_image_url.com'}
    ]
  },
  'dates': {
    'created': '6 days ago',
    'updated': '6 days ago',
    'resolved': '6 days ago'
  }
}
```

## Exercise: Finding Popular Tickets

Lists and dictionaries often work together. Notice how the `people` field in the random ticket is a dictionary,
containing a `watchers` key, which holds a list. For this exercise, your goal is to filter the list of 250 tickets down
to only the **most popular tickets**—those with 8 or more watchers.

### Task: Write a Function to Find Popular Tickets

```python
def get_popular_tickets(tickets):
    """
    From a list of tickets, return all tickets with 8 or 
    more "watchers".
    """
    popular_tickets = []
    for ticket in tickets:
        if len(ticket['people']['watchers']) >= 8:
            popular_tickets.append(ticket)

    return popular_tickets


# Filter the popular tickets
popular = get_popular_tickets(big_tickets)

# Test the function
assert len(popular) > 0  # There should be at least one popular ticket

# Ensure each popular ticket has 8 or more watchers
for ticket in popular:
    assert len(ticket['people']['watchers']) >= 8

print("Nice job! Your function works correctly.")
```

Output:

```plaintext
Nice job! Your function works correctly.
```

### Solution

In case you need a reference, here's the solution:

```python
def get_popular_tickets_solution(tickets):
    """
    From a list of tickets, return all tickets with 8 or 
    more "watchers".
    """
    popular_tickets = []
    for ticket in tickets:
        num_watchers = len(ticket['people']['watchers'])
        if num_watchers >= 8:
            popular_tickets.append(ticket)
    return popular_tickets  
```