package db

import (
	"context"
	"fmt"
	"go/types"
	"log"
	"sync"

	"github.com/libp2p/go-libp2p/core/host"
	"github.com/libp2p/go-libp2p/core/peer"
	"github.com/multiformats/go-multiaddr"
)

func bootstrap(ctx context.Context, dht *dht.IpfsDHT) {
	//Bootstrap
	log.Println("[DHT] Running bootstrap thread")
	if err := dht.Bootstrap(ctx); err != nil {
		log.Println("[DHT] Fail to bootstrap DHT: ", err)
	}

}

func init_DHT(ctx context.Context, host host.Host, config types.Config) *dht.IpfsDHT {
	// init DHT

	kademliaDHT, err := dht.New(ctx, host)
	if err != nil {
		log.Println("[DHT] Fail to init DHT: ", err)
	}
	log.Println("[DHT] Init sucsesfull")
	return kademliaDHT

}

func boot(ctx context.Context, randevu string, host host.Host) {
	if randevu == "" {
		return
	}
	log.Println("[DHT:Bootstrap] Running bootstrap from config: ", randevu)
	// Parse configuration
	sourceMultiAddr, err := multiaddr.NewMultiaddr(fmt.Sprintf(randevu))
	if err != nil {
		log.Println("[DHT:Bootstrap] Fail to parse multiaddr: ", err)
	}

	// Conver the multiaddr to peerinfo
	var wg sync.WaitGroup
	peerinfo, err := peer.AddrInfoFromP2pAddr(sourceMultiAddr)
	if err != nil {
		log.Println("[DHT:Bootstrap] Fail to parse multiaddr: ", err)
	}
	wg.Add(1)
	go func() {
		defer wg.Done()

		if err := host.Connect(ctx, *peerinfo); err != nil {
			log.Println("[DHT:Bootstrap] Fail to connect:", err)
		} else {
			log.Println("[DHT:Bootstrap] Successfully connected to node: ", *peerinfo)
		}
	}()
	wg.Wait()

}
