# S.D WaterProofing Django Rest API

**Empowering S.D WaterProofing's Portfolio and Helpdesk System**

Welcome to the S.D WaterProofing Django Rest API repository! This API powers S.D WaterProofing's portfolio showcase and helpdesk ticketing system. Explore our previous work, and easily submit helpdesk tickets for support. Built with Django and Django-REST-Framework (DRF)

Check out [API documentation](http://api-sd-waterproofing.abhisheksurela.in/) and start contributing today!

## Table of Contents

- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)


## Getting Started

Before you start using the API, make sure you have the following prerequisites:

1. Python (version 3.11.1)
2. Django (version 4.2.3)
3. Django Rest Framework (version 3.14.0)


### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/abhisheksurela79/API-SD-WATER-PROOFING.git
   ```


2. Install Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

Now the API should be up and running locally at [localhost](http://localhost:8000/).


#API Endpoints

The API provides the following endpoints:

1. `/portfolio/` Get a list of portfolio items.
2. `/helpdesk/` Raise a ticket.



#Contributing

Contributions to this project are welcome! If you find any issues or have improvements to suggest, please create a GitHub issue or submit a pull request.
