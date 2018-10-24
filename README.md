# PureProof 

Purer email though cryptographic proof of work. Creative application allows for an adaptable and scale-able solution.

Made at TigerHacks 2018. See it on [DevPost](https://devpost.com/software/pureproof).

## Inspiration

Spam emails drives everyone nuts. On top of this, all of our filtering systems are based on heuristics: they more-or-less guess. However, what if we introduced a small but non-zero cost to send an email? Everyday people wouldn't notice much impact, but it would on the scale of millions of spam emails.

## What it does

An email recipient can set an amount of work that they expect to be done on all emails they receive. If this work is not done, then they can reject or sort the email based on this status. Effectively, sending an email is now tied to very real and limited physical resources.

## How we built it

Basic SMTP and IMAP email clients are build in Python using Asciimatics for the GUI. This enabled us to have low level control over the client side operation without having to spend the entire weekend digging through documentation for Thunderbird or Google Apps.

The Server's backend also in Python, but of course all the other web-goodness (HTML, CSS, JS).

The actual proof-of-work has to be carefully crafted, as to prevent a malicious email sender from stacking things in their favor. For example, one may try to reuse proof of work, save up proof of work for later use, or try to decrease the
general amount of work needed.

## Challenges we ran into

Mail servers are super stingy and limiting, as they are trying to prevent the same things we are solving. But this ironically makes testing difficult.

## Accomplishments that we're proud of

The development process was rather long and had lots of discussion. The mentors were amazing and provided lots of invaluable feedback. Without that, we wouldn't have made the same decisions.

To a degree, the system was planned out much more than needed for a hackathon. However, this does help in selling the system beyond just the implemented proof-of-concept, and it also meant that we didn't have any major architectural issues during the implementation.

## What we learned

Asciimatics (a terminal graphics program), sanic (a new asynchronous webserver), and that sometimes you just need plain javascript.

## What's next for PureProof

From the beginning, part of the design was to provide a way for the system to scale and seamlessly operate, from just a few users to entire mail servers. With a clear path for technical adoption, it would be feasible to move this system forward to its end goal. We think it would be amazing if this system caught on and began cleaning up our mailboxes.
