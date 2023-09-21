#!/usr/bin/env python3

import csv
import re


def contains_domain(address, domain):
    """Check if the email address contains the given domain."""
    domain_pattern = r'[\w\.-]+@' + domain + '$'
    return re.match(domain_pattern, address) is not None


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    return re.sub(old_domain_pattern, new_domain, address)


def update_email_domains(user_email_list, old_domain, new_domain):
    """Update the emails in the list by changing the old domain to the new domain."""
    old_domain_email_list = []
    new_domain_email_list = []
    
    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)

    return old_domain_email_list, new_domain_email_list


def update_user_data(user_data_list, old_domain_email_list, new_domain_email_list):
    """Update the users in the list using the new domain emails."""
    email_key = 'Email Address'
    email_index = user_data_list[0].index(email_key)
    
    for user in user_data_list[1:]:
        for old_email, new_email in zip(old_domain_email_list, new_domain_email_list):
            if user[email_index] == old_email:
                user[email_index] = new_email

    return user_data_list


def process_file(file_path, old_domain, new_domain):
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    with open(file_path, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

        old_domain_email_list, new_domain_email_list = update_email_domains(user_email_list, old_domain, new_domain)
        updated_user_data = update_user_data(user_data_list, old_domain_email_list, new_domain_email_list)
        
    return updated_user_data


def write_updated_data_to_csv(file_path, updated_data):
    """Writes updated data to a CSV file."""
    with open(file_path, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(updated_data)


def main():
    home_dir = '/home/<student-id>/data/'
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = home_dir + 'user_emails.csv'
    report_file = home_dir + 'updated_user_emails.csv'
    
    updated_data = process_file(csv_file_location, old_domain, new_domain)
    write_updated_data_to_csv(report_file, updated_data)


if __name__ == "__main__":
    main()
