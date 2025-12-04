package com.example.mymod;

import com.mojang.logging.LogUtils;
import net.minecraft.client.Minecraft;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.TextComponent;
import net.minecraft.network.chat.style.Style;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.api.distmarker.OnlyIn;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.eventbus.api.EventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaMod;

/**
 * This is the main mod class that will contain all the code for your mod.
 */
@Mod("mymod")
public class MyMod
{
    // Create a logger instance to log to the console
    private static final LogUtils LOGGER = LogUtils.getLogger();

    // Create the entry point for the mod
    public MyMod()
    {
        // Register the commonSetup method for modloading
        IEventBus modEventBus = MinecraftForge.EVENT_BUS;

        // Register the commonSetup method for modloading
        modEventBus.addListener(this::commonSetup);

        // Register the Deferred Register to the mod event bus so items can be registered
        modEventBus.addListener(this::onRegisterItems);

        // You can use SubscribeEvent and let the Event Bus discover all methods to call on the mod
        // Event Bus can discover methods to call on it
        modEventBus.addListener(this::onServerStarting);
    }

    private void commonSetup(final FMLCommonSetupEvent event)
    {
        // Some common setup code
        LOGGER.info("HELLO FROM COMMON SETUP");
        LOGGER.info("DIRT BLOCK >> {}", ForgeRegistries.BLOCKS.getKey(ForgeRegistries.BLOCKS.getValue(new ResourceLocation("minecraft:dirt"))));
    }

    private void onServerStarting(ServerStartingEvent event)
    {
        // Some server starting logic
        LOGGER.info("HELLO FROM SERVER START");
    }

    private void onRegisterItems(final DeferredRegister<Item> items)
    {
        // Register an item for use in the game
        items.register("example_item", () -> new Item(new Item.Properties()));
    }
}
modLoader="javafml"
loaderVersion="[40,)" 
license="MIT"
issueTrackerURL="https://github.com/example/my-mod/issues"

[[mods]]
modId="mymod"
version="1.0.0"
displayName="My Mod"
description='''My first mod for Minecraft'''
authors="Your Name"
