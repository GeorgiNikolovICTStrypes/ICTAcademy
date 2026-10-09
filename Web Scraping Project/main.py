'''
This module is the entry point for the web scraping project.
It initializes a scraping sessoin and calls the start method
'''
from session_logic.scraping_session import ScrapingSession

session = ScrapingSession()
session.start()
