# SeRa

To improve food and nutrition security in Mali, it is important that farmers and family farms in Mali have knowledge about, and access to quality seeds for cereal crops. Due to several limitations that some farmers have, the current system of buying and selling seeds still needs some improvements. Given that a few of these limitations are low literacy and a lack of internet access, we have come up with a project called SeRa. With SeRa we hope to support the current work of the AOPP by offering both farmers and OP’s the opportunity to use a voice-based interface. The key idea of this project is that SeRa offers a database in which all the product information will be stored. This database is connected to a voice server that can be used by both OP’s and farmers to either upload or retrieve information by phoning in. This adds value to the current work of AOPP, as it will be audio-based and therefore use of the internet or reading/writing skills will not be necessary.

## Architecture

The figure shows the layout or network configuration of the interactions between the parties:

![SeRa architecture](/assets/architecture.png)

SeRa’s users will interact with the system via two different voice interfaces accessible through basic/feature phones and a web interface:

- Upload Interface (voice): this will be used by OPs without internet access in order for them to create/update announcements by specifying the seed category, bulk price, and quantity (in kilos). Every area has a dedicated interface.
- Search Interface (voice): this will be used by individual farmers and OPs in order to browse recent seed offerings by category, price, and quantity. Every area has a dedicated interface.
- Web Interface: this will be used both by farmer unions and radio operators. Union accounts will be able to create/update/retrieve seed offerings through a browser Radio accounts will use the interface to download batches of announcements in audio format in order to broadcast them.

![Interactions](/assets/interactions.png)
