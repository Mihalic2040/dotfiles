package db

import (
	"context"
	"fmt"
	"go/types"
	"log"
	"sync"

	dht "github.com/libp2p/go-libp2p-kad-dht"
	"github.com/libp2p/go-libp2p/core/host"
	"github.com/libp2p/go-libp2p/core/peer"
	"github.com/multiformats/go-multiaddr"
)

func InitDb(ctx context.Context, host host.Host) {
	kademliaDHT, err := dht.New(ctx, host)
	if err != nil {
		panic(err)
	}

	return kademliaDHT
}

func bootstrap(ctx context.Context, dht *dht.IpfsDHT) {
	//Bootstrap
	log.Println("[DHT] Running bootstrap thread")
	if err := dht.Bootstrap(ctx); err != nil {
		log.Println("[DHT] Fail to bootstrap DHT: ", err)
	}

}

func init_DHT(ctx context.Context, host host.Host, config types.Config) *dht.IpfsDHT {
	// init DHT

	if config.DHTServer == true {
		kademliaDHT, err := dht.New(ctx, host, dht.Mode(dht.ModeAutoServer))
		if err != nil {
			log.Println("[DHT] Fail to init DHT: ", err)
		}
		log.Println("[DHT:Server MODE] Init sucsesfull")
		return kademliaDHT
	} else {
		kademliaDHT, err := dht.New(ctx, host)
		if err != nil {
			log.Println("[DHT] Fail to init DHT: ", err)
		}
		log.Println("[DHT] Init sucsesfull")
		return kademliaDHT
	}

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
