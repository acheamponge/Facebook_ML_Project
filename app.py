import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.aboutkm
import src.pages.about
import src.pages.ads
import src.pages.comments
import src.pages.apps
import src.pages.games
import src.pages.events
import src.pages.follow
import src.pages.friends
import src.pages.information
import src.pages.interaction
import src.pages.likes
import src.pages.location
import src.pages.marketplace
import src.pages.groups
import src.pages.polls
import src.pages.pages
import src.pages.posts
import src.pages.search
import src.pages.profiles
import src.pages.resources
import src.pages.places
import src.pages.messages
import src.pages.payments
import src.pages.photos
import src.pages.portal
import src.pages.saved


MENU = {
    "Home" : src.pages.home,
    "About Kwame Technologist" : src.pages.aboutkm,
    "Ads & Businesses" : src.pages.ads,
    "Apps & Websites" : src.pages.apps,
    "Comments" : src.pages.comments,
    "Events" : src.pages.events,
    "Facebook Gaming" : src.pages.games,
    "Following & Followers" : src.pages.follow,
    "Friends" : src.pages.friends,
    "Groups" : src.pages.groups,
    "Information Used for Recommendations" : src.pages.information,
    "Interactions" : src.pages.interaction,
    "Likes & Reactions" : src.pages.likes,
    "Location" : src.pages.location,
    "Marketplace" : src.pages.marketplace,
    "Messages" : src.pages.messages,
    "Other Activity" : src.pages.polls,
    "Pages" : src.pages.pages,
    "Payment History" : src.pages.payments,
    "Photos and Videos" : src.pages.photos,
    "Portal" : src.pages.portal,
    "Posts" : src.pages.posts,
    "Profile Information" : src.pages.profiles,
    "Saved Items and Collections" : src.pages.saved,
    "Search History" : src.pages.search,
    "Voice Recording and Transcription" : src.pages.voices,
    "Places" : src.pages.places,
}

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

if __name__ == "__main__":
    main()
